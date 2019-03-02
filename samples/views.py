from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
from geopy.geocoders import GoogleV3
from .models import SampleStatus, SampleDetails, SampleResults
from checkout.models import Order
from .forms import SampleResultsForm, SampleDetailsForm
from django.core.mail import send_mail
from django.core.paginator import Paginator
import os

User = get_user_model()

@login_required
def yourportal(request):
    """Gives access to the users sample history and reports"""
    details = SampleDetails.objects.all()
    complet_filter = Q(status='Complete') & Q(ordered_by=request.user)
    all_completed_samples = SampleStatus.objects.filter(complet_filter)
    completed_paginator = Paginator(all_completed_samples, 10)
    page_completed = request.GET.get('page_completed', 1)
    completed_samples = completed_paginator.page(page_completed)
    processing_filter = ~Q(status='Complete') & Q(ordered_by=request.user)
    all_processing_samples = SampleStatus.objects.filter(processing_filter)
    processing_paginator = Paginator(all_processing_samples, 10)
    processing_page = int(request.GET.get('processing_page', 1))
    processing_samples = processing_paginator.page(processing_page)

    arg = {"processing_samples": processing_samples,
           "completed_samples": completed_samples,
           "details": details}

    return render(request, 'yourportal.html', arg)

@login_required()
def details(request):
    """Opens form to submit sample details"""

    if request.method == 'POST':
        sample_ref =  request.POST['sample_ref']

        try:
            sample = SampleStatus.objects.get(sample_ref=sample_ref)
            if sample.status == 'Dispatched':

                details_form = SampleDetailsForm()

                arg = {'details_form': details_form,
                       'sample': sample}

                return render(request,
                              "submitdetails.html",
                              arg)
            else:
                msg = '{0}{1}{2}{3}'.format(
                    sample_ref,
                    ' is not available to be "Submitted",',
                    ' it may not have been dispatched yet',
                    ' or has already been processed')

                messages.error(request, msg)
            return redirect(yourportal)
        except SampleStatus.DoesNotExist:
            msg = '{0} is not a valid sample reference'.format(sample_ref)
            messages.error(request, msg)
        pass
    else:
        messages.error(request, 'Not POST')
    return redirect(yourportal)



@login_required()
def submit(request, sample_id):
    """Submits user inputed sample details"""

    if request.method == 'POST':
        details_form = SampleDetailsForm(request.POST)
        sample =  SampleStatus.objects.get(id=sample_id)
        if details_form.is_valid():

            sample.submitted_by = request.user
            sample.submit_date = timezone.now()
            sample.status = 'Submitted'
            sample.save()

            details = details_form.save(commit=False)
            details.save()
            geolocator = GoogleV3(api_key=os.getenv('GOOGLE_MAP_API_KEY'))
            lat_lng = (details.sample_location.latitude,
                       details.sample_location.longitude)
            sample_address = geolocator.reverse(lat_lng)
            details.sample_address = sample_address[0]
            details.sample = sample
            details.save()
            return redirect(yourportal)

    else:
        details_form = SampleDetailsForm()
        arg = {'details_form': details_form,
               'sample': sample}
    return render(request, "submitdetails.html", arg)

@login_required()
def viewreport(request, sample_id):
    """Renders report with sample details and results"""

    os.getenv('GOOGLE_MAP_API_KEY')
    if request.method == 'POST':
        try:
            status = SampleStatus.objects.get(id=sample_id)
            details = SampleDetails.objects.get(sample=status)
            results = SampleResults.objects.get(sample=status)
            p_perc = (results.p/12)*100
            k_perc = (results.k/200)*100
            ph_perc = (results.ph/12)*100
            lr_ph_perc = (results.lr_ph/12)*100

        except SampleStatus.DoesNotExist:
            print("Sample ID does not exist")
        except SampleDetails.DoesNotExist:
            print("Can not find sample details")
        except SampleResults.DoesNotExist:
            results = ""
            p_perc = ""
            k_perc = ""
            ph_perc = ""
            lr_ph_perc = ""
        pass

        arg = {'status': status,
               'details': details,
               'results': results,
               'p_perc' : p_perc,
               'k_perc' : k_perc,
               'ph_perc' : ph_perc,
               'lr_ph_perc' : lr_ph_perc,
               }

        return render(request, "viewreport.html", arg)

    else:
        error_message = "You do not have access to this url"

    arg = {'GOOGLE_MAP_API_KEY': os.getenv('GOOGLE_MAP_API_KEY'),
           'status': "",
           'details': "",
           'results': "",
           'error_message': error_message}

    return render(request, "viewreport.html", arg)

@staff_member_required
def labportal(request):
    """Renders view to lab managment system.
    Staff can record samples as being dispatched to customer, received into
    lab, can upload test results and can search the sample archive"""

    all_samples = SampleStatus.objects.all()
    paginator = Paginator(all_samples, 10)
    page = request.GET.get('page', 1)
    arg = {"samples": paginator.page(page),
           'results_form': SampleResultsForm(),
           'username': request.user.username}

    return render(request, 'labportal.html', arg)


@staff_member_required
def dispatch(request):
    """Records an inputed sample reference as dispatched to customer"""

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
                msg = '{0} has already been dispatched'.format(sample_ref)
                messages.error(request, msg)
            return redirect(labportal)
        except SampleStatus.DoesNotExist:
            msg = '{0} is not a valid sample reference'.format(sample_ref)
            messages.error(request, msg)
        pass

    return redirect(labportal)


@staff_member_required
def receive(request):
    """Records an inputed sample reference as
    received into the lab for analysis"""

    if request.method == 'POST':
        sample_ref =  request.POST['sample_ref']
        try:
            sample = SampleStatus.objects.get(sample_ref=sample_ref)
            if sample.status == "Submitted":

                sample.status = 'Received'
                sample.received_by = request.user
                sample.received_date = timezone.now()
                sample.save()
                msg = '{0} has been recorded as "Received"'.format(sample_ref)
                messages.success(request, msg)
            else:
                msg = '{0}{1}{2}{3}'.format(
                    sample_ref,
                    ' is not available to be "Received",',
                    ' it may not have been "Submitted yet" or',
                    'has already been processed')

                messages.error(request, msg)
            return redirect(labportal)
        except SampleStatus.DoesNotExist:
            msg = '{0} is not a valid sample reference'.format(sample_ref)
            messages.error(request, msg)
        pass

    return redirect(labportal)

@staff_member_required
def results(request):
    """Upload results of a sample test"""

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
                          results_email(user.username),
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

def results_email(username):
    """Return email content to be sent to customer when their
    results are complete"""
    email_content = """\
    Hi {0},

    Your soil test results are complete and available to view.

    Just log into 'Your Portal':

    https://dc-easca-environmental.herokuapp.com/yourportal

    Regards,

    Dan Casey

    Lab Rat
    Easca Environmental

    """.format(username)
    return email_content
