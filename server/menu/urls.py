
from django.urls import path
from .import views

urlpatterns = [
    path('menu-items',views.ListMenuItemsView,name='menu-items'),
    path('cart-items',views.CartItemsView,name='cart-items'),
    path('get-current-user',views.CartItemsView,name='get-current-user'),
    path('remove-order/<int:id>',views.RemoveOrderView,name='remove-order'),
    path('place-order',views.PlaceOrderView,name='place-order'),
]

