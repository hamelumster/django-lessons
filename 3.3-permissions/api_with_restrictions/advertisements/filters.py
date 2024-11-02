import django_filters
from django_filters import rest_framework as filters

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at_before = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")
    created_at_after = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at_before', 'created_at_after', 'creator']
