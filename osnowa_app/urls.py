from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$', views.point_list, name='point_list'),
#link ma prowadzić do strony ze szczegółami o punkcie
	url(r'^point/(?P<pk>[0-9]+)/$', views.point_detail, name='point_detail'),
	url(r'^point/new/$', views.point_new, name='point_new'),
]

