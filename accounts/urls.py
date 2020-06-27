from accounts.views import home_view, signup_view, login_view, results_view, panel_view,  user_show, mylogin_view, form_view
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^home/$', home_view, name="home"),
    url(r'^signup/$', signup_view, name="signup"),
    url(r'^formlogin/$', login_view, name ="login"),
    url(r'^results/$', results_view, name= "results"),
    url(r'^panel/$', panel_view, name = 'panel'),   
    url(r'^user/$', user_show, name = 'user'),
    url(r'^logins/$', mylogin_view, name = 'mylogin'),
    url(r'^form/$', form_view, name = 'form')
]
