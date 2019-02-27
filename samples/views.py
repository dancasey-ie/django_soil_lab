from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.conf import settings
from django.db import models
from django.utils import timezone
from geopy.geocoders import GoogleV3
from .models import SampleStatus, SampleDetails, SampleResults
from checkout.models import Order
from .forms import SampleResultsForm, SampleDetailsForm
from django.core.mail import send_mail
from django.contrib.auth import get_user_model



import os
User = get_user_model()
@login_required
def yourportal(request):
    """A view that displays the profile page of a logged in user"""
    statuss = SampleStatus.objects.filter(ordered_by=request.user)
    details = SampleDetails.objects.all()
    return render(request, 'yourportal.html', {"statuss": statuss, "details": details})

@login_required()
def submit(request, status_id):
    """A view that manages the customer sample submission form"""

    status = SampleStatus.objects.get(id=status_id)
    if request.method == 'POST':
        details_form = SampleDetailsForm(request.POST)

        if details_form.is_valid():
            status = SampleStatus.objects.get(id=status_id)
            status.submitted_by = request.user
            status.submit_date = timezone.now()
            status.status = 'Submitted'
            status.save()

            details = details_form.save(commit=False)
            details.save()
            geolocator = GoogleV3(api_key=os.getenv('GOOGLE_MAP_API_KEY'))
            sample_address = geolocator.reverse((details.sample_location.latitude,
                                                         details.sample_location.longitude))
            details.sample_address = sample_address[0]
            details.sample = status
            details.save()
            return redirect(yourportal)

    else:
        details_form = SampleDetailsForm()

    return render(request, "submitdetails.html", {'details_form': details_form, 'status': status})

@login_required()
def viewreport(request, sample_id):
    os.getenv('GOOGLE_MAP_API_KEY')
    if request.method == 'POST':
        try:
            status = SampleStatus.objects.get(id=sample_id)
            details = SampleDetails.objects.get(sample=status)
            results = SampleResults.objects.get(sample=status)

        except SampleStatus.DoesNotExist:
            print("Sample ID does not exist")
        except SampleDetails.DoesNotExist:
            print("Can not find sample details")
        except SampleResults.DoesNotExist:
            print("Results pending")
            results = ""
        pass
        return render(request, "viewreport.html", {'status': status, 'details': details,'results': results})

    else:
        error_message = "You do not have access to this url"
        status = ""
        details = ""
        results = ""
    return render(request, "viewreport.html",
                  {'GOOGLE_MAP_API_KEY': os.getenv('GOOGLE_MAP_API_KEY'),
                                               'status': status,
                                               'details': details,
                                               'results': results,
                                               'error_message': error_message})

@staff_member_required
def labportal(request):
    samples = SampleStatus.objects.all()
    results_form = SampleResultsForm()
    username = request.user.username
    return render(request, 'labportal.html', {"samples": samples, 'results_form': results_form, 'username': username})

@staff_member_required
def dispatch(request):

    if request.method == 'POST':
        sample_ref =  request.POST['sample_ref']
        try:
            sample = SampleStatus.objects.get(sample_ref=sample_ref)
            if sample.status == 'Ordered':
                sample.status = 'Dispatched'
                sample.dispatched_by = request.user
                sample.dispatched_date = timezone.now()
                sample.save()
            else:
                messages.error(request, '{0} has already been dispatched'.format(sample_ref))
            return redirect(labportal)
        except SampleStatus.DoesNotExist:
            messages.error(request, '{0} is not a valid sample reference'.format(sample_ref))
        pass

    return redirect(labportal)
@staff_member_required
def receive(request):

    if request.method == 'POST':
        sample_ref =  request.POST['sample_ref']
        try:
            sample = SampleStatus.objects.get(sample_ref=sample_ref)
            if sample.status == "Submitted":

                sample.status = 'Received'
                sample.received_by = request.user
                sample.received_date = timezone.now()
                sample.save()
                messages.success(request, '{0} has been recorded as "Received"'.format(sample_ref))
            else:
                messages.error(request,
                               '{0} is not available to be "Received", it may not have been "Submitted yet" or has already been processed'.format(sample_ref))
            return redirect(labportal)
        except SampleStatus.DoesNotExist:
            messages.error(request, '{0} is not a valid sample reference'.format(sample_ref))
        pass

    return redirect(labportal)

@staff_member_required
def results(request):
    if request.method == 'POST':
        results_form = SampleResultsForm(request.POST)
        if results_form.is_valid():
            results = results_form.save(commit=False)
            results.save()
            sample = results.sample
            sample.status = 'Complete'
            sample.tested_by = request.user
            sample.tested_date = timezone.now()
            sample.save()
            try:
                user = User.objects.get(username=sample.ordered_by)
                send_mail('Sample Results',
                          'Easca Environmental would like to inform you that new results are available to you.Follow the link to your portal to access the results. https://dc-easca-environmental.herokuapp.com/yourportal ',
                          'eascatest@gmail.com',
                          [user.email],
                          fail_silently=False,
                          )
            except User.doesNotExists:
                messages.error(request, 'email failed to send, no user found')
            return redirect(labportal)


    else:
        results_form = SampleResultsForm()
    return redirect(labportal)
