from rest_framework import serializers
from .models import Tools

class ToolsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tools
        fields = ('id', 'title', 'url', 'description')