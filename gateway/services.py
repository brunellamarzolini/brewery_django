import requests
from rest_framework.response import Response
from rest_framework import status

def fetch_external_api(serializer_class, query_params, api_url, error_message):
    serializer = serializer_class(data=query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.get(api_url, params=serializer.validated_data, timeout=5)
        response.raise_for_status()
        return Response(response.json(), status=response.status_code)

    except requests.Timeout:
        return Response(
            {"error": "External API Request Timeout."},
            status=status.HTTP_504_GATEWAY_TIMEOUT
        )

    except requests.RequestException:
        return Response(
            {"error": error_message},
            status=status.HTTP_502_BAD_GATEWAY
        )
