from django.contrib import admin
from .models import SampleStatus, SampleDetails, SampleResults, Sample, Soil1Results, Soil2Results

admin.site.register(Sample)
admin.site.register(Soil1Results)
admin.site.register(Soil2Results)

admin.site.register(SampleStatus)
admin.site.register(SampleDetails)
admin.site.register(SampleResults)