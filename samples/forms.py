from django import forms
from .models import Sample, Soil1Results, SampleStatus


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
        widgets = {
            'sample_date': forms.DateInput(attrs={'class':'datepicker'}),
        }

class Soil1ResultsForm(forms.ModelForm):
    class Meta:
        model = Soil1Results
        fields = ('sample',
                  'recieved_by',
                  'recieved_date',
                  'sample_condition',
                  'batch_no',
                  'test_start_date',
                  'p_morgan_result',
                  'k_morgan_result',
                  'lr_ph_result',
                  'ph_result',
                  'lab_comments',
                  'test_end_date',
                  'tested_by')
        widgets = {
            'recieved_date': forms.DateInput(attrs={'class':'datepicker'}),
            'test_start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'test_end_date': forms.DateInput(attrs={'class':'datepicker'}),
        }

#class RecieveSampleForm(forms.ModelForm):
  #  class Meta:
  #      model = SampleStatus
    #    fields = ('sample',)

