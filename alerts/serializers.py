from rest_framework import serializers
# from alerts.common.alert import Alert
from alerts.models import Alert

from brine.constants import INVALID_REQUEST

class AlertListSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='status'
    )
    created_by = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Alert
        fields = ("id", "price", "created_by", "status")

class AlertSerializer(serializers.Serializer):
    price = serializers.IntegerField(required=True)
    status = serializers.CharField(max_length=200, required=False)
    created_by = serializers.CharField(max_length=200,required=False)
    is_active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Alert.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.price = validated_data.get("price", instance.price)
        instance.status = validated_data.get("status", instance.status)
        instance.created_by = validated_data.get("created_by", instance.created_by)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance
       
    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.price = attrs.get("price", instance.price)
            instance.status = attrs.get("status", instance.status)
            instance.created_by = attrs.get("created_by", instance.created_by)
            instance.is_active = attrs.get("is_active", instance.is_active)
            return instance
    
        return Alert(**attrs)
    
    def validate(self, data):
        if 3<1:
            raise serializers.ValidationError(INVALID_REQUEST)
        return data
    # class Meta:
    #     model = Alert
    #     fields = '__all__'