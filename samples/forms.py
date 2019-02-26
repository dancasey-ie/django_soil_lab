from django import forms
from .models import SampleResults, SampleDetails


class SampleDetailsForm(forms.ModelForm):
    class Meta:
        model = SampleDetails
        fields = ('customer_name',
                  'customer_ref_1',
                  'customer_ref_2',
                  'sample_location',
                  'sample_date',
                  'soil_type',
                  'land_use',
                  'other_comments',)

        widgets = {
            'sample_date': forms.DateInput(attrs={'class':'datepicker'}),
        }


class SampleResultsForm(forms.ModelForm):
    class Meta:
        model = SampleResults
        fields = ('sample',
                  'p',
                  'k',
                  'lr_ph',
                  'ph',)


