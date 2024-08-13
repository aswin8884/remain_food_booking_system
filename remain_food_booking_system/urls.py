
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index),
    path("login",views.login),
    path("registration_users",views.registration_users),
    path("registration_caters",views.registration_caters),
    path("registration_restaurants",views.registration_restaurants),
    path("admin_home",views.admin_home),
    path("caters_home",views.caters_home),
    path("restaurant_home",views.restaurant_home),
    path("user_home",views.user_home),
    path("view_caters_requests",views.view_caters_requests),
    path("view_restaurants_requests",views.view_restaurants_requests),
    path("accept_caters",views.accept_caters),
    path("reject_caters",views.reject_caters),
    path("accept_restaurants",views.accept_restaurants),
    path("reject_restaurants",views.reject_restaurants),
    path("view_caters",views.view_caters),
    path("view_restaurants",views.view_restaurants),
    path("view_users",views.view_users),
    path("delete_caters",views.delete_caters),
    path("delete_restaurants",views.delete_restaurants),
    path("delete_users",views.delete_users),
    path("sell_food_restaurants",views.sell_food_restaurants),
    path("view_food_uploads_restaurants",views.view_food_uploads_restaurants),
    path("cancel_food_restaurant",views.cancel_food_restaurant),
    path("view_restaurant_requests_admin",views.view_restaurant_requests_admin),
    path("accept_restaurant_food_request",views.accept_restaurant_food_request),
    path("reject_restaurant_food_request",views.reject_restaurant_food_request),
    path("accept_caters_food_request",views.accept_caters_food_request),
    path("reject_caters_food_request",views.reject_caters_food_request),
    path("payment_restaurant_food",views.payment_restaurant_food),
    path("payment_confirm_restaurant_food",views.payment_confirm_restaurant_food),
    path("view_bookings_admin_restaurants",views.view_bookings_admin_restaurants),
    path("view_bookings_admin_caters",views.view_bookings_admin_caters),
    path("view_bookings_admin_restaurants",views.view_bookings_admin_restaurants),
    path("sell_food_caters",views.sell_food_caters),
    path("view_food_uploads_caters",views.view_food_uploads_caters),
    path("cancel_food_caters",views.cancel_food_caters),
    path("view_caters_requests_admin",views.view_caters_requests_admin),
    path("payment_caters_food",views.payment_caters_food),
    path("payment_confirm_caters_food",views.payment_confirm_caters_food),
    path("view_foods_admin",views.view_foods_admin),
    path("add_food_admin_restaurant",views.add_food_admin_restaurant),
    path("add_food_admin_caters",views.add_food_admin_caters),
    path("upload_food_admin",views.upload_food_admin),
    path("book_food_user",views.book_food_user),
    path("view_bookings_user",views.view_bookings_user),
    path("check_out_user",views.check_out_user),
    path("payment_page_user",views.payment_page_user),
    path("view_bookings_food_restaurants",views.view_bookings_food_restaurants),
    path("view_bookings_food_caters",views.view_bookings_food_caters),
    path("view_bookings_users_admin",views.view_bookings_users_admin),
    path("add_feedbacks_user",views.add_feedbacks_user),
    path("view_feedbacks_user",views.view_feedbacks_user),
    path("view_foods_user",views.view_foods_user),
    path("search_foods",views.search_foods),

]
