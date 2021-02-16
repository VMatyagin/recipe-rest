from rest_framework import serializers

from core.models import Area, Boec, Brigade, Shtab


class ShtabSerializer(serializers.ModelSerializer):
    """serializer for the shtab objects"""

    class Meta:
        model = Shtab
        fields = ('id', 'title')
        read_only_fields = ('id',)


class AreaSerializer(serializers.ModelSerializer):
    """serializer for area objects"""

    class Meta:
        model = Area
        fields = ('id', 'title', 'shortTitle')
        read_only_fields = ('id',)


class BoecSerializer(serializers.ModelSerializer):
    """serializer for boec objects"""

    class Meta:
        model = Boec
        fields = ('id', 'firstName', 'lastName', 'middleName', 'DOB')
        read_only_fields = ('id',)


class BrigadeSerializer(serializers.ModelSerializer):
    """serializer for brigade objects"""
    boec_count = serializers.SerializerMethodField('get_boec_count')

    def get_boec_count(self, obj):
        return obj.boec.count()

    class Meta:
        model = Brigade
        fields = ('id', 'title', 'shtab', 'area', 'DOB', 'boec', 'boec_count')
        read_only_fields = ('id', 'boec_count',)