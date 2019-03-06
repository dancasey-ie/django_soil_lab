from .models import SampleStatus
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = SampleStatus
        fields = ['sample_ref', 'username', 'status', ]
