from .models import RandomPost
from rest_framework import serializers

class RandomPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RandomPost
        fields = ('first','second','creation_date')
        