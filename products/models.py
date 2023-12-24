from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name='نام دسته بندی')
    
    def __str__(self) -> str:
        super(Category, self).__str__()
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'






class Food(models.Model):
    TYPES: list[tuple[str, str]] = [
        ('fast-food', 'فست فود'),
        ('drink', 'نوشیدنی'),
        ('salad', 'سالاد'),
    ]
    
    to = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    name = models.CharField(max_length=90, null=True, blank=True,verbose_name='نام غذا')
    price = models.CharField(max_length=15, null=True, blank=True,verbose_name='قیمت')
    image = models.ImageField(upload_to='images/foods', null=True, blank=True, verbose_name='عکس')
    quantity = models.IntegerField(default=10, null=True, blank=True,verbose_name='تعداد')
    ingredients = models.TextField(max_length=150, null=True, blank=True, verbose_name='مواد اولیه')
    food_type = models.CharField(max_length=50, choices=TYPES, null=True, blank=True, verbose_name='نوع غذا')
    
    def __str__(self) -> str:
        super(Food, self).__str__()
        return self.name
    
    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذاها'
        
        




class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    
    def __str__(self) -> str:
        super(Cart, self).__str__()
        return str(self.user)
    
    class Meta:
        verbose_name = 'لیست سبد خرید'






class CartItems(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(to=Food, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='غذا')
    
    def __str__(self) -> str:
        super(CartItems, self).__str__()
        return str(self.cart)
    
    class Meta:
        verbose_name = 'آیتم های سبد خرید'