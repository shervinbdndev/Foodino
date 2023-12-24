import datetime

from django.shortcuts import render
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from products.models import Food







class FoodinoView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        year: int = datetime.datetime.now().year
        foods: Food = Food.objects.all()
        
        return render(
            request=request,
            template_name='index.html',
            context={
                'current_year': year,
                'foods': foods,
            },
        )
        
        

class FoodinoContactUsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        year: int = datetime.datetime.now().year
        
        return render(
            request=request,
            template_name='contact.html',
            context={
                'current_year': year,
            },
        )