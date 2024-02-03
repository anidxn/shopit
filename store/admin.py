from django.contrib import admin
from . import models
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Customer)
admin.site.register(models.Order)
# ---- for the auto profile creation ---------
admin.site.register(models.Profile)

# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = models.Profile

# extend the User model & specify which columns to display in Admin panel
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name','last_name', 'email']  # columns that come from User Model
    inlines = [ProfileInline]

# As we are modifying the existing Admin User module, we need to unregister the model & re-register
admin.site.unregister(User)

# Reregister with the new view columns
admin.site.register(User, UserAdmin)