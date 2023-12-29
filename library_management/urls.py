
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('category/<slug:category_slug>', views.Home, name='category_wise'),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('transactions/', include('transactions.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)