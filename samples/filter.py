from .models import SampleStatus
from django.conf import settings
from django import forms
import django_filters


class SampleFilter(django_filters.FilterSet):
    sample_ref = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SampleStatus
        fields = ['sample_ref', 'status', 'ordered_by']
