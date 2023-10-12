from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import CreateAPIView

from api.serializers import CreateRateSerializer


class CreateRateView(CreateAPIView):
    authentication_classes = (BasicAuthentication,)
    serializer_class = CreateRateSerializer
