from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^signup/v1.0$', views.signup, name='signup'),
    url(r'^login/v1.0$', views.login, name='account_login'),
   ]