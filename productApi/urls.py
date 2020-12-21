from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'signup', views.SignupViewSet)
router.register(r'login', views.LoginViewSet)
router.register(r'plant', views.PlantViewSet)
router.register(r'order', views.OrderViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browse able API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

