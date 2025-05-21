from rest_framework import serializers

class BreweryListQuerySerializer(serializers.Serializer):
    by_name = serializers.CharField(required=False)
    by_country = serializers.CharField(required=False)
    by_state = serializers.CharField(required=False)
    by_type = serializers.CharField(required=False)

    per_page = serializers.IntegerField(
        required=False,
        min_value=1,
        max_value=200,
        error_messages={
            "max_value": "Maximum allowed value for per_page is 200.",
            "min_value": "Minimum value for per_page is 1."
        }
    )

    page = serializers.IntegerField(
        required=False,
        min_value=1,
        error_messages={
            "min_value": "Page must be 1 or higher."
        }
    )

    sort = serializers.ChoiceField(
        required=False,
        choices=[
            "city:asc",
            "city:desc",
            "name:asc",
            "name:desc"
        ],
        error_messages={
            "invalid_choice": "Sort must be one of 'city:asc', 'city:desc', 'name:asc', or 'name:desc'."
        }
    )

class BreweryMetaQuerySerializer(serializers.Serializer):
    by_name = serializers.CharField(required=False)
    by_country = serializers.CharField(required=False)
    by_state = serializers.CharField(required=False)
    by_type = serializers.CharField(required=False)