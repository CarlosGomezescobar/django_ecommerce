from django.contrib import admin
from django.urls import path
from core import views
#from core import AdminViews
from django.conf.urls.static import static
# from django.conf import settings
from ecom import settings

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('admin_login/', views.adminLogin, name="admin_login"),
    path('admin_login_process/', views.adminLoginProcess,
         name="admin_login_process"),
    path('admin_logout_process/', views.adminLogoutProcess,
         name="admin_logout_process"),

    path('adminhome/', views.adminhome, name="adminhome"),

]