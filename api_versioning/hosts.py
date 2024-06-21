from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'api_versioning.urls', name='default'),
    host(r'v1', 'version1.urls', name='v1'),
    host(r'v2', 'version2.urls', name='v2'),
)