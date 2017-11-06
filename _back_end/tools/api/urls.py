from django.conf.urls import url, include
from core.views import ToolsListView, ToolsDetails
from rest_framework import routers

router = routers.DefaultRouter()
router.register('^', ToolsListView)

helper_patterns = [
    url(r'^tools', include(router.urls)),
    url(r'^details', ToolsDetails.get)
]

urlpatterns = helper_patterns