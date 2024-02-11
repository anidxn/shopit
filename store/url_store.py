
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutpage, name='about-us'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='sign-up'),
    path('update_profile/', views.update_profile, name='update-profile'),
    path('logout/', views.logout_user, name='logout'),
    path('product/<int:pk>', views.product_detail, name='product'),
    path('prodbycat/<str:catname>', views.product_by_cat, name='prodbycat'),
]