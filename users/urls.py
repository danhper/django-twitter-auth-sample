from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include

from .views import UserLoginCallback, UserLoginRedirect, profile


oauth_patterns = patterns('',
    url(r'^(?P<provider>(\w|-)+)/$',
        UserLoginRedirect.as_view(),
        name='user-login'),
    url(r'^callback/(?P<provider>(\w|-)+)/$',
        UserLoginCallback.as_view(),
        name='user-login-callback'),
)

urlpatterns = patterns('',
    url(r'^oauth/', include(oauth_patterns)),

    url(r'^profile/$', login_required(profile)),
)
