
from django.urls import include, path

urlpatterns = [
    path('v1/', include("arlo.v1.urls")),
]