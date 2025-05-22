from rest_framework import serializers

COUNTRY_CHOICES = [
    'Austria',
    'England',
    'France',
    'Isle of Man',
    'Ireland',
    'Poland',
    'Portugal',
    'Scotland',
    'Singapore',
    'South Korea',
    'United States',
]

TYPE_CHOICES = [
    'micro',       # Most craft breweries. E.g., Samuel Adams.
    'nano',        # Extremely small, local distribution.
    'regional',    # Regional location of an expanded brewery.
    'brewpub',     # Beer-focused restaurant/bar with brewery on-premise.
    'large',       # Very large brewery. (deprecated)
    'planning',    # Brewery in planning or not yet open.
    'bar',         # Bar, no brewery equipment. (deprecated)
    'contract',    # Uses another brewery’s equipment.
    'proprietor',  # Brewery incubator.
    'closed',      # Location has been closed.
]

class BreweryListQuerySerializer(serializers.Serializer):
    by_name = serializers.CharField(required=False)
    by_country = serializers.ChoiceField(
        required=False,
        choices=COUNTRY_CHOICES,
        error_messages={
            "invalid_choice": f"Country must be one of: {', '.join(COUNTRY_CHOICES)}."
        }
    )
    by_state = serializers.CharField(required=False)
    by_type = serializers.ChoiceField(
        required=False,
        choices=TYPE_CHOICES,
        error_messages={
            "invalid_choice": (
                "Type must be one of: micro, nano, regional, brewpub, large, planning, "
                "bar, contract, proprietor, closed."
            )
        }
    )
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
    by_country = serializers.ChoiceField(
        required=False,
        choices=COUNTRY_CHOICES,
        error_messages={
            "invalid_choice": f"Country must be one of: {', '.join(COUNTRY_CHOICES)}."
        }
    )    
    by_state = serializers.CharField(required=False)
    by_type = serializers.ChoiceField(
        required=False,
        choices=TYPE_CHOICES,
        error_messages={
            "invalid_choice": (
                "Type must be one of: micro, nano, regional, brewpub, large, planning, "
                "bar, contract, proprietor, closed."
            )
        }
    )