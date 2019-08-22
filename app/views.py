# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests 
from rest_framework.response import Response
from .models import PerformanceMetric
from io import StringIO
from .serializers import PerformanceDataSerializer as pSerializer
from .filters import DataFilter
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
import csv

# API Call that stores data in psql
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def get_data(request):
    if request.method == 'GET':
        r = requests.get('https://gist.githubusercontent.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv')
        f = StringIO(r.text)
        reader = csv.DictReader(f)
        for row in reader:
            PerformanceMetric.objects.get_or_create( 
                date=row['date'],
                channel=row['channel'],
                country=row['country'],
                os = row['os'],
                impressions= row['impressions'],
                clicks = row['clicks'],
                installs= row['installs'],
                spend= row['spend'],
                revenue=row['revenue'],
            )
    return Response({'ok'})


# Filtering Api
class PerformanceListFilter(ListAPIView):
    serializer_class = pSerializer
    paginate_by = 25
    queryset = PerformanceMetric.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DataFilter
    permission_classes = (AllowAny,)



    def get_queryset(self):
        queryset = self.queryset.extra(select={"cpi": "spend/installs"})
        fields = [field.name for field in PerformanceMetric._meta.get_fields()]
        fields.append('cpi')
        return queryset