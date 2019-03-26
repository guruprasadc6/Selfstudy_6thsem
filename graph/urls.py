from django.conf.urls import url
from graph import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^history/$', views.history, name='history'),
	url(r'^predict/$', views.predict, name='predict'),
]