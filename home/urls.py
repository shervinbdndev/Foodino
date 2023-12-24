from django.urls import path

from . import views



urlpatterns = [
    path(
        route='',
        view=views.FoodinoView.as_view(),
        name='index',
    ),
    
    path(
        route='contact-us',
        view=views.FoodinoContactUsView.as_view(),
        name='contact',
    ),
]