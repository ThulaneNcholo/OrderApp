
from django.urls import path
from .import views

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('increase-qty/<int:id>',views.IncreaseQuantityView,name='increase-qty'),
    path('decrease-qty/<int:id>',views.DecreaseQuantityView,name='decrease-qty'),
    path('update-cart/<int:id>',views.UpdateCartView,name='update-cart'),

    # specials urls 
    path('increase-special-qty/<int:id>',views.IncreaseSpecialQuantityView,name='increase-special-qty'),
    path('decrease-special-qty/<int:id>',views.DecreaseSpecialQuantityView,name='decrease-special-qty'),
]

