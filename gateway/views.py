from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from gateway.serializer import BreweryListQuerySerializer, BreweryMetaQuerySerializer
from gateway.services import fetch_external_api

BREWERY_API_BASE_URL = getattr(settings, "BREWERY_API_BASE_URL", None)
BREWERY_API_BASE_URL_META = getattr(settings, "BREWERY_API_BASE_URL_META", None)

class BreweryList(APIView):
    @extend_schema(
        parameters=[BreweryListQuerySerializer],
    )
    def get(self, request):
        return fetch_external_api(
            BreweryListQuerySerializer,
            request.query_params,
            BREWERY_API_BASE_URL,
            "Failed to fetch breweries"
        )

class BreweryMeta(APIView):
    @extend_schema(
        parameters=[BreweryMetaQuerySerializer],
    )
    def get(self, request):
        return fetch_external_api(
            BreweryMetaQuerySerializer,
            request.query_params,
            BREWERY_API_BASE_URL_META,
            "Failed to fetch metadata"
        )
