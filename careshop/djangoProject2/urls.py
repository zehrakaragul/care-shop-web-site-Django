from django.contrib import admin
from django.urls import path, include



urlpatterns = [
  path('', include('pages.urls')),
  path('shops/', include('shop.urls')),
  path('account/', include('account.urls')),
  path('admin/', admin.site.urls),

]

#djangoProject2
#shop
#pages