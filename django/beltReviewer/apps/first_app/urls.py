from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^welcome$', views.welcome),    # This line has changed!
    url(r'^register', views.register),
    url(r'^login', views.login),
    # url(r'^this_app/new$', views.new, name = 'my_new'),
    url(r'^first_app/home$', views.home, name='home'),
    url(r'^first_app/BookAndReview$', views.BookAndReview, name='bk_review'),
    url(r'^addBookAndReview', views.addBookAndReview),
    url(r'^first_app/logout$', views.logout, name='logout'),


     # url(r'^first_app/this_book(?P<id>\d+)$', views.this_book, name = 'this_book')

]