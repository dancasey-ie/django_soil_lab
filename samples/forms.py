from django import forms
from .models import Sample

class SampleCustomerForm(forms.ModelForm):
    class Meta:
        model = Sample
        # varibles defined in Order model
        fields = ('sample_ref', 'analysis_req', 'location',
                  'sample_date', 'customer_ref', 'soil_type',
                  'land_use', 'other_comments')

class SampleStaffForm(forms.ModelForm):
    class Meta:
        model = Sample
        # varibles defined in Order model
        fields = ('sample_condition', 'recieved_date',
                  'test_start_date', 'test_end_date', 'status')