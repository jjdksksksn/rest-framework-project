from rest_framework import serializers
from .models import Ads, Post

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')