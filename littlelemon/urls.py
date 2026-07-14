from django.contrib import admin
from django.urls import path, include
from restaurant.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    # Static HTML home page
    path('', index, name='index'),

    # Restaurant app API (menu-items, bookings, api-token-auth)
    path('api/', include('restaurant.urls')),

    # Djoser authentication / registration endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
