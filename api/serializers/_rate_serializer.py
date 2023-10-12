from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from core.models import Rate


class CreateRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ("post", "score")

    def get_user(self):
        request = self.context.get("request")
        if request:
            return request.user
        return None

    def validate(self, data):
        user = self.get_user()
        if not user or not user.is_authenticated:
            raise ValidationError("In order to set rating, you must login first")
        return super(CreateRateSerializer, self).validate(data)

    def create(self, validated_data):
        user = self.get_user()
        try:
            obj = Rate.objects.get(user=user)
            obj.score = validated_data["score"]
            obj.save()
        except ObjectDoesNotExist:
            obj = Rate.objects.create(user=user, **validated_data)
        return obj
