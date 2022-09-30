from rest_framework import serializers
from .models import Test
class NewsIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('title',)
