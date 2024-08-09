from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="about_shop"),
    path("contact/", views.contact, name="contact_shop"),
    path("check_out/", views.check_out, name="checkout_shop"),
    path("products/<int:myid>", views.product_view, name="Product_View"),
]
