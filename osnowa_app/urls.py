from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$', views.point_list, name='point_list'),
]
