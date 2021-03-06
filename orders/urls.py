from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("ajax", views.ajax, name="ajax"),
    path("addtocart", views.addtocart, name="addtocart"),
    path("shoppingcart", views.shoppingcart, name="shoppingcart"),
    path("checkout", views.checkout, name="checkout"),
    path("clear", views.clear, name="clear"),
    path("clean", views.clean, name="clean")
]
