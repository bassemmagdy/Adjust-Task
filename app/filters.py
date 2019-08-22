from django_filters.rest_framework import FilterSet, CharFilter, DateFilter
from .models import PerformanceMetric
from rest_framework.filters import BaseFilterBackend

from django.db.models import Sum, Avg, Count
from rest_framework.exceptions import APIException

class DataFilter(FilterSet):
    
    ##  Filters Vars   
    start_date = DateFilter(field_name='date',lookup_expr='gte') 
    end_date = DateFilter(field_name='date', lookup_expr='lte')
    date = DateFilter(field_name='date', lookup_expr='exact')
    channel = CharFilter(method='channel_filter')
    country = CharFilter(method='country_filter')
    os =  CharFilter(method='os_filter')


    ##  Grouping Vars   
    grouping_by = CharFilter(method='group_by_filter')


    ## Ordering Vars
    order_by_date = CharFilter(method='order_by_date_filter')
    order_by_channel = CharFilter(method='order_by_channel_filter')
    order_by_country = CharFilter(method='order_by_country_filter')
    order_by_os = CharFilter(method='order_by_os_filter')
    order_by_impressions = CharFilter(method='order_by_impressions_filter')
    order_by_clicks = CharFilter(method='order_by_clicks_filter')
    order_by_installs = CharFilter(method='order_by_installs_filter')
    order_by_spend = CharFilter(method='order_by_spend_filter')
    order_by_revenue = CharFilter(method='order_by_revenue_filter')
    order_by_cpi = CharFilter(method='order_by_cpi_filter')


    ##  Filters
    def channel_filter(self, queryset, name, value):
        return queryset.filter(channel__icontains=value)
    
    def country_filter(self, queryset, name, value):
        return queryset.filter(country__icontains=value)

    def os_filter(self, queryset, name, value):
        return queryset.filter(os__icontains=value)
    
    
    ## Grouping by
    def group_by_filter(self, queryset, name, value):
        cols = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue','cpi']
        params = [x.strip() for x in value.split(',')]
        # paramas.append('cpi')
        for x in params:
            if x not in cols:
                raise APIException("Whoops! you are using wrong parameters in group by filter")
            else:
                pass
        return queryset.values(*params).annotate(clicks=Sum('clicks'), impressions=Sum('impressions'), installs=Sum('installs'), revenues=Sum('revenue'))

    
    ##  Ordering by
    def order_by_date_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('date')
        else:
            return queryset.order_by('-date')

    def order_by_channel_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('channel')
        else:
            return queryset.order_by('-channel')
    
    def order_by_country_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('country')
        else:
            return queryset.order_by('-country')

    def order_by_os_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('os')
        else:
            return queryset.order_by('-os')

    def order_by_impressions_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('impressions')
        else:
            return queryset.order_by('-impressions')

    def order_by_clicks_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('clicks')
        else:
            return queryset.order_by('-clicks')

    def order_by_installs_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('installs')
        else:
            return queryset.order_by('-installs')

    def order_by_spend_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('spend')
        else:
            return queryset.order_by('-spend')

    def order_by_revenue_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('revenue')
        else:
            return queryset.order_by('-revenue')
    
    def order_by_cpi_filter(self, queryset, name, value):
        if value == 'asc':
            return queryset.order_by('cpi')
        else:
            return queryset.order_by('-cpi')
    
    class Meta:

        model = PerformanceMetric
        fields = 'channel', 'country', 'impressions', 'clicks', 'date', 'spend', 'os', 'revenue', 'installs',