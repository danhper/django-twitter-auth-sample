from django.shortcuts import render

from allaccess.views import OAuthCallback

from django.core.urlresolvers import reverse
from allaccess.views import OAuthRedirect


class UserLoginRedirect(OAuthRedirect):
    def get_callback_url(self, provider):
        return reverse('user-login-callback', kwargs={'provider': provider.name})


class UserLoginCallback(OAuthCallback):
    def get_login_redirect(self, provider, user, access, new=False):
        if new:
            info = access.api_client.get_profile_info(access.access_token)
            name = info["name"].split(' ', 1)
            user.first_name = name[0]
            if len(name) > 1:
                user.last_name = name[1]
            user.username = info["screen_name"]
            user.save()
        return super(UserLoginCallback, self).get_login_redirect(provider, user, access, new)


def profile(request):
    return render(request, 'profile.html', { "user": request.user })
