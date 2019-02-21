from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from .models import Sample, Soil1Results
from .forms import SampleCustomerForm, Soil1ResultsForm

@login_required
def yourportal(request):
    """A view that displays the profile page of a logged in user"""
    samples = Sample.objects.filter(user=request.user)
    return render(request, 'yourportal.html', {"samples": samples})

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
def viewreport(request, sample_id):

    if request.method == 'POST':
        try:
            sample = Sample.objects.get(id=sample_id)
            results = ""
            return render(request, "viewreport.html", {'sample': sample, 'results': results})
        except Sample.DoesNotExist:
            print("Sample ID does not exist")
        pass

    else:
        error_message = "You do not have access to this url"
        sample = ""
    return render(request, "viewreport.html", {'sample': sample, 'error_message': error_message})


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
    samples = Sample.objects.all()
    return render(request, 'labportal.html', {"samples": samples})

