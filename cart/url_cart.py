from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart-summary'),      # view cart
    path('add/', views.cart_add, name='cart-add'),      # view cart
    path('delete/', views.cart_delete, name='cart-delete'),      # delete an item from cart using ajax
    path('update/', views.cart_update, name='cart-update'),      # update an item quantity using ajax
]