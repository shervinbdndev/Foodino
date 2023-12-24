from django.urls import path

from . import views



urlpatterns = [
    path(
        route='foods',
        view=views.ProductListView.as_view(),
        name='foods',
    ),
    
    path(
        route='cart',
        view=views.CartDetails.as_view(),
        name='cart',
    ),
    
    path(
        route='foods/add/<id>',
        view=views.ProductAddToCart.as_view(),
        name='add',
    ),
]