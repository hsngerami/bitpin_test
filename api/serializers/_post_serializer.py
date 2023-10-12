from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    number_of_users = serializers.SerializerMethodField()
    average_score = serializers.SerializerMethodField()
    user_score = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title

    def get_number_of_users(self, obj):
        return obj.number_of_users

    def get_average_score(self, obj):
        return obj.average_score

    def get_user_score(self, obj):
        return obj.user_score