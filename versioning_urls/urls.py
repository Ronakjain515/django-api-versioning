from django.urls import path, re_path

from .views import URLPathVersioningClassAPIView, AcceptHeaderVersioningClassAPIView, \
    QueryParamterVersioningClassAPIView, HostNameVersioningClassAPIView

urlpatterns = [
    re_path(
        r'^(?P<version>(v1|v2))/urlVersion',
        URLPathVersioningClassAPIView.as_view(),
        name='bookings-list'
    ),
    path(
        'acceptheaderVersioning',
        AcceptHeaderVersioningClassAPIView.as_view(),
        name='bookings-list'
    ),

    path(
        'queryparamterVersioning',
        QueryParamterVersioningClassAPIView.as_view(),
        name='bookings-list'
    ),
    path(
        'hostnameVersioning',
        HostNameVersioningClassAPIView.as_view(),
        name='bookings-list'
    ),
]