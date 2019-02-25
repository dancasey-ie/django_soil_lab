from django.contrib import admin
from .models import SampleStatus, SampleDetails, SampleResults

admin.site.register(SampleStatus)
admin.site.register(SampleDetails)
admin.site.register(SampleResults)