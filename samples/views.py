from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from .models import Sample, Soil1Results, SampleStatus, SampleDetails, SampleResults
from .forms import SampleCustomerForm, Soil1ResultsForm, SampleResultsForm, SampleDetailsForm, SampleStatusForm
import os

@login_required
def yourportal(request):
    """A view that displays the profile page of a logged in user"""
    statuss = SampleStatus.objects.filter(submitted_by=request.user)
    details = SampleDetails.objects.all()
    return render(request, 'yourportal.html', {"statuss": statuss, "details": details})

@login_required()
def newsample(request):
    """A view that manages the customer sample submission form"""
    if request.method == 'POST':
        sample_form = SampleCustomerForm(request.POST)
        if sample_form.is_valid():
            sample = sample_form.save(commit=False)
            sample.submit_date = timezone.now()
            sample.user = request.user
            sample.save()
            return redirect(yourportal)

    else:
        sample_form = SampleCustomerForm()

    return render(request, "sampledetails.html", {'sample_form': sample_form})

@login_required()
def submit(request):
    """A view that manages the customer sample submission form"""
    if request.method == 'POST':
        status_form = SampleStatusForm(request.POST)
        details_form = SampleDetailsForm(request.POST)
        if status_form.is_valid() and details_form.is_valid():
            status = status_form.save(commit=False)
            status.submitted_by = request.user
            status.submit_date = timezone.now()
            status.status = 'Submitted'
            status.save()


            details = details_form.save(commit=False)
            details.save()
            details.sample = status
            details.save()
            return redirect(yourportal)

    else:
        status_form = SampleStatusForm()
        details_form = SampleDetailsForm()

    return render(request, "submitdetails.html", {'status_form': status_form,
                                                  'details_form': details_form})

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
def labdetails(request):
    """A view that manages the customer sample submission form"""
    if request.method == 'POST':
        results_form = Soil1ResultsForm(request.POST)
        if results_form.is_valid():
            results = results_form.save(commit=False)
            results.save()
            return redirect(labportal)

    else:
        results_form = Soil1ResultsForm()

    return render(request, "labdetails.html", {'results_form': results_form})

@staff_member_required
def labportal(request):
    samples = SampleStatus.objects.all()
    results_form = SampleResultsForm()
    return render(request, 'labportal.html', {"samples": samples, 'results_form': results_form})

@staff_member_required
def receive(request):

    if request.method == 'POST':
        sample_ref =  request.POST['sample_ref']
        try:
            sample = SampleStatus.objects.get(sample_ref=sample_ref)
            sample.status = 'Received'
            sample.received_by = request.user
            sample.received_date = timezone.now()
            sample.save()
            return redirect(labportal)
        except SampleStatus.DoesNotExist:
            error_message = "Not a valid Sample Reference"
            print("Not a valid Sample Reference")
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
            sample.test_date = timezone.now()
            sample.save()
            return redirect(labportal)

    else:
        print("Error in results form")
    return redirect(labportal)
