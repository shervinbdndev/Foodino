from typing import Union

from django.urls.base import reverse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from .models import Food, Cart, CartItems





class ProductListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        foods: Food = Food.objects.all()
        
        return render(
            request=request,
            template_name='products/foods.html',
            context={
                'foods': foods,    
            },
        )
        
        




class ProductAddToCart(View):
    def get(self, request: HttpRequest, id: str) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
        if (not request.user.is_authenticated):
            return redirect(to=reverse('login'))
        
        food: Food = Food.objects.get(id=id)
        
        cart, _ = Cart.objects.get_or_create(
            user=request.user,
            is_paid=False,
        )
        cart_items: CartItems = CartItems.objects.create(
            cart=cart,
            product=food,
        )
        cart_items.save()
        
        context_cart_items = CartItems.objects.filter(cart__is_paid = False, cart__user = request.user)
        
        request.session['cart_items_count'] = context_cart_items.count()
        
        return HttpResponseRedirect(redirect_to=request.META.get('HTTP_REFERER'))
    
    




class CartDetails(View):
    def get(self, request: HttpRequest) -> HttpRequest:
        if (not request.user.is_authenticated):
            return redirect(to=reverse('login'))
        
        return render(
            request=request,
            template_name='products/cart.html',
            context={
                
            }
        )