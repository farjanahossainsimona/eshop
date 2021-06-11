from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('account/', include('account.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
