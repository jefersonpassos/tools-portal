from django.conf.urls import url, include
from core.views import ToolsListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('^tools', ToolsListView)

helper_patterns = [
    url(r'^', include(router.urls))
]

urlpatterns = helper_patterns