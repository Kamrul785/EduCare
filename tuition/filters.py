from django_filters.rest_framework import FilterSet
from .models import Tuition

class TuitionFilter(FilterSet):
    class Meta:
        model = Tuition
        fields = {
            'class_level': ['icontains'],
            'subject': ['icontains'],
            'tutor': ['exact']
        }