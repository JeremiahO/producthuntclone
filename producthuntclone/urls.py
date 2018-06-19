from django.contrib import admin
from django.urls import path, include
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # This allows us to see the products view from its app
    path('',views.home, name='home'),
    # This directs all traffic related to acounts to the accounts url.py
    path('accounts/',include('accounts.urls')),
]
