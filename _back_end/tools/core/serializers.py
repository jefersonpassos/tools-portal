from rest_framework import serializers
from .models import Tools
import json

from django.core import serializers as djangoSerializer

from django.db.models import Count
from django.db.models import Avg
from django.db.models import Max
from django.db.models import FloatField


class ToolsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tools
        fields = ('id', 'title', 'url', 'description')


class ToolsDetailsSerializer():
    
    def groupByTitle():
        
        data = Tools.objects.values('title').annotate(maxID=Max('id'))
        # data = Tools.objects.raw("Select count(title) as total from core_tools group by title")]
        # data = Tools.objects.all().aggregate(Max=('id'))
        return data