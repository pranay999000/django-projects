from rest_framework import fields, serializers
from . models import Country

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name', 'area', 'capital'
        )