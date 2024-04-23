from rest_framework import serializers

from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    # profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    # def get_profile(self, obj):
    #     profile = Profile.objects.get(user=obj)
    #     return ProfileSerializer(profile).data
