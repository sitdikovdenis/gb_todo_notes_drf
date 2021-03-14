from django_filters import rest_framework as filters
from .models import Project,TODO


class ProjectFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Project
       fields = ['name']


class TODOFilter(filters.FilterSet):
   project = filters.ModelChoiceFilter(queryset=Project.objects.all())
   date_from = filters.DateFromToRangeFilter(field_name='created_at')

   class Meta:
       model = TODO
       fields = ['project']
