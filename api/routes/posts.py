from django.db.models import Count, Avg, Case, When, IntegerField
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed

from api.serializers import PostListSerializer

from core.models import Post


class PostListView(ListAPIView):
    authentication_classes = (BasicAuthentication,)
    serializer_class = PostListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.all().annotate(
                number_of_users=Count("rates__owner"),
                average_score=Avg("rates__score"),
                user_score=Case(
                    When(rates__user=user, then='rates__score'),
                    default=None,
                    output_field=IntegerField()
                ),
            )
        raise AuthenticationFailed()
