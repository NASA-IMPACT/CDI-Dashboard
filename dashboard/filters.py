from django_filters import FilterSet, DateFilter, CharFilter, ChoiceFilter, ModelChoiceFilter

from .models import Masterlist


class MasterlistFilter(FilterSet):
	title = CharFilter(label='Title', field_name='title', lookup_expr='icontains')
	organization = CharFilter(label='Organization', field_name='organization', lookup_expr='icontains')
	cdi_themes = CharFilter(label='Themes', field_name='cdi_themes', lookup_expr='icontains')

	class Meta:
		model = Masterlist
		fields = ['title', 'organization', 'cdi_themes', 'status', 'metadata_type']
