import re

from rest_framework import versioning


class ParameterQueryVersioningClass(versioning.QueryParameterVersioning):
    default_version = '1.0'
    allowed_version = ['1.1', '1.2']
    version_param = 'version'


class URLPathVersioningClass(versioning.URLPathVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'


class AcceptHeaderVersioningClass(versioning.AcceptHeaderVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'


class NameSpaceVersioningClass(versioning.NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'


class QueryParameterVersioningClass(versioning.QueryParameterVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2']
    version_param = 'version'


class HostNameVersioningClass(versioning.HostNameVersioning):
    def get_version(self, request):
        match = re.match(r'^(.*?)(?:\.(?!.*\.(?:api|beta|dev)).*)?$',
                         request.get_host())
        if match:
            return match.group(1).strip('.').split('.')[0]
        return None
