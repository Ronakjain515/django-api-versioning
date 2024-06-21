from django.urls import path, re_path

from .views import Version2ClassAPIView

app_name = "v2"
urlpatterns = [
    path(
        'namespaceVersioning',
        Version2ClassAPIView.as_view(),
        name='bookings-list'
    ),
    path(
        'hostnameVersioning',
        Version2ClassAPIView.as_view(),
        name='bookings-list'
    )
]