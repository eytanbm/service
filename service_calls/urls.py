from django.conf.urls import patterns, include, url
from django.contrib import admin

from service_calls.api.urls import urlpatterns as api_urls
from service_calls.content.urls import urlpatterns as content_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'service_calls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^content/', include(content_urls)),
    url(r'^api/', include(api_urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url('^', include('django.contrib.auth.urls'))
)
