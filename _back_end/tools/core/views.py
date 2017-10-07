from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Tools
from .serializers import ToolsSerializer

class ToolsListView(ModelViewSet):
    
    serializer_class = ToolsSerializer
    queryset = Tools.objects.all()

    def get_queryset(self):
        
        queryset = Tools.objects.all()

        url = self.request.query_params.get('url', None)
        if(url):
            queryset = queryset.filter(url=url)
        
        return queryset
