from django.contrib import admin
from django.urls import path, include
from . import views

# References
# How to Create a Login System in Python Using Django? | Python Projects | GeeksforGeeks (2021) Available at: https://www.youtube.com/watch?v=1UvTNMH7zDo (accessed 10 October 2022).

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('add_asset', views.add_asset, name="add_asset"),
    path('save_asset', views.save_asset, name="save_asset"),
    path('edit_asset/<asset_id>', views.edit_asset, name="edit_asset"),
    path('delete_asset/<asset_id>', views.delete_asset, name="delete_asset"),
    path('all_assets', views.all_assets, name="all_assets"),
]