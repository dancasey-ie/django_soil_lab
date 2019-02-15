from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Sample
from .forms import SampleCustomerForm


@login_required()
def newsample(request):
    """A view that manages the customer sample submission form"""
    if request.method == 'POST':
        sample_form = SampleCustomerForm(request.POST)
        if sample_form.is_valid():
            sample = sample_form.save(commit=False)
            sample.submit_dat = timezone.now()
            sample.username = request.user
            sample.sav()

    else:
        sample_form = SampleCustomerForm()

    return render(request, "soilsamplesubmit.html", {'sample_form': sample_form})

def submitsample(request):

    return render(request, 'profile.html')