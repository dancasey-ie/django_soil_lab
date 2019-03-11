from .models import SampleStatus
from django.conf import settings
from django import forms
import django_filters

class SampleFilter(django_filters.FilterSet):
   # sample_ref = django_filters.CharFilter(lookup_expr='icontains')
  # sample_ref = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
  # status = django_filters.ChoiceFilter(lookup_expr='exact', choices= SampleStatus.STATUS_CHOICES , widget=forms.Select(attrs={'class': 'form-control'}))
  #  ordered_by = django_filters.ChoiceFilter(lookup_expr='exact', choices=USER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = SampleStatus
        fields = ['sample_ref', 'status', 'ordered_by']
