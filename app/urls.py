from app.views import data_views, show_views, edit_views, update_views, delete_views
from django.conf.urls import url

# Create youur urls here.

urlpatterns = [

    url(r'^student/$', data_views, name = 'data'),
    url(r'^show/$',show_views, name = 'show'),
    url(r'^edit/<int:id>/$', edit_views, name = 'edit'),
    url(r'^update/<int:id>/$', update_views, name = 'update'),
    url(r'^delete/<int:id>/$', delete_views, name = 'delete'),
    
]