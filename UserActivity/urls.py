from django.urls import include, path
from rest_framework import routers
from IndexApp import views
router = routers.DefaultRouter()
router.register(r'useractivity', views.MemberViewSet)
# router.register(r'activity', views.ActivityViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
