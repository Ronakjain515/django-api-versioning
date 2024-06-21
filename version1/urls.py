from django.urls import path, re_path

from .views import Version1ClassAPIView

app_name = "v1"
urlpatterns = [
    path(
        'namespaceVersioning',
        Version1ClassAPIView.as_view(),
        name='bookings-list'
    ),
    path(
        'hostnameVersioning',
        Version1ClassAPIView.as_view(),
        name='bookings-list'
    )
]