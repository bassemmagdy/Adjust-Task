from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import get_data, PerformanceListFilter


router = DefaultRouter()
urlpatterns = [
    path('get_data/', get_data, name='get_data'),
    path('performance/', PerformanceListFilter.as_view(), name='performance'),

]

urlpatterns.extend(router.urls)
