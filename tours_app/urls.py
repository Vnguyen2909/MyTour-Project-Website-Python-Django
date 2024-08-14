from django.urls import path
from . import views

app_name = "natours"

urlpatterns = [
    path("", views.index, name="index"),
    path("create_tour", views.create_tour, name="create-tour"),
    path("detail_tour/<tour_id>", views.detail_tour, name="detail-tour"),
    path("update_tour/<tour_id>", views.update_tour, name="update-tour"),
    path("delete_tour/<tour_id>", views.delete_tour, name="delete-tour"),
    path("type_tour/<type_id>", views.type_tour, name="type-tour"),
    path("all_type_tour", views.all_type_tour, name="all-type-tour"),
    path("create_type_tour", views.create_type_tour, name="create-type-tour"),
    path(
        "delete_type_tour/<type_tour_id>",
        views.delete_type_tour,
        name="delete-type-tour",
    ),
    path("create_profile", views.create_profile, name="create-profile"),
    # path("update_profile", views.update_profile, name="update-profile"),
    path("update_profile", views.update_profile, name="update-profile"),
    path("add_photo", views.add_photo, name="add-photo"),
    path("add_to_cart", views.add_to_cart, name="add-to-cart"),
    path("all_my_cart", views.all_my_cart, name="all_my_cart"),
    path("delete_cart_item/<tour_id>", views.delete_cart_item, name="delete-cart-item"),
    path("check_out", views.check_out, name="check-out"),
    path("place_order", views.place_order, name="place-order"),
    path("all_my_orders", views.all_my_orders, name="all_my_orders"),
    path("detail_order/<order_id>", views.detail_order, name="detail-order"),
    path("update_order/<order_id>", views.update_order, name="update-order"),
    path("refuse_order/<order_id>", views.refuse_order, name="refuse-order"),
    path("delete-order/<order_id>", views.delete_order, name="delete-order"),
]
