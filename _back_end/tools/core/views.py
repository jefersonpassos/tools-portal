from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# decorator for http methods
from django.views.decorators.http import require_http_methods

# HTTP
from django.http import HttpResponse, JsonResponse

# model
from .models import Tools

# serializer
from .serializers import ToolsSerializer, ToolsDetailsSerializer


# class view for api_rest_framework
class ToolsListView(ModelViewSet):
    
    serializer_class = ToolsSerializer
    queryset = Tools.objects.all()

    def get_queryset(self):
        
        queryset = Tools.objects.all()

        url = self.request.query_params.get('url', None)
        raw = self.request.query_params.get('raw', None)
        
        if(url):
            queryset = queryset.filter(url=url)
        elif(raw):
            queryset = Tools.objects.raw("Select id, count(title) as total from core_tools group by title")

        
        return queryset
        

class ToolsDetails():
    
    @require_http_methods(["GET"])
    def get(self):
        return HttpResponse(ToolsDetailsSerializer.groupByTitle())