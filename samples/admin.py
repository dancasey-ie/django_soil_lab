from django.contrib import admin
from .models import Sample, ResultsLineItem

class ResultsLineAdminInLine(admin.TabularInline):
    model = ResultsLineItem

class SampleAdmin(admin.ModelAdmin):
    inlines = [ResultsLineAdminInLine]

admin.site.register(Sample, SampleAdmin)