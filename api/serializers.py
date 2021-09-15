from rest_framework import serializers

from .models import Site, StatusVals, Pivot



class SiteListSerializer(serializers.ModelSerializer):

    # status = serializers.BooleanField()

    class Meta:
        model = Site
        fields = '__all__'

class SiteDetailSerializer(serializers.ModelSerializer):

    statuses = serializers.SlugRelatedField(slug_field='value', read_only=True)


    class Meta:
        model = Site
        fields = '__all__'

class SiteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class CreateStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusVals
        fields = '__all__'

    def create(self, validated_data):
        stauts = StatusVals.objects.update_or_create(
            updated_at=validated_data.get('updated_at', None),
            site=validated_data.get('site', None),
            defaults={'status': validated_data.get('status')}
        )
        return stauts