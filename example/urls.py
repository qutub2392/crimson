from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^contact/$', views.contact, name='contact'),

]
