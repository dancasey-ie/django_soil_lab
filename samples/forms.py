from django import forms
from .models import Sample

class SampleCustomerForm(forms.ModelForm):
    class Meta:
        model = Sample
        # varibles defined in Order model
        fields = ('sample_ref',
                  'customer_name',
                  'customer_ref_1',
                  'customer_ref_2',
                  'sample_location',
                  'sample_date',
                  'analysis_req',
                  'soil_type',
                  'land_use',
                  'other_comments')

class SampleStaffForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('sample_condition',
                  'recieved_date',
                  'recieved_by',
                  'batch_no',
                  'test_start_date',
                  'test_end_date',
                  'tested_by',
                  'status')