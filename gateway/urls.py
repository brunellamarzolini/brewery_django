from django.urls import path
from .views import BreweryList, BreweryMeta

urlpatterns = [
    path('breweries/', BreweryList.as_view(), name='brewery-list'),
    path('breweries/meta', BreweryMeta.as_view(), name='brewery-meta'),
]