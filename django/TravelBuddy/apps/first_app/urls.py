from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^welcome$', views.welcome) ,   # This line has changed!
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^addTrip', views.add_plan),
    url(r'^first_app/new_trip$', views.add_plan_link, name = 'add_plan'),
    # url(r'^this_app/new$', views.new, name = 'my_new'),
    url(r'^first_app/logout$', views.logout, name='logout'),
    url(r'^first_app/home$', views.home, name='home'),
     # url(r'^first_app/this_book(?P<id>\d+)$', views.this_book, name = 'this_book')

]

