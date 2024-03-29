from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('translate/', include('translate.urls')),
    path('category/', include('category.urls')),
    path('dictation/', include('dictation.urls')),
    path('accounts/', include('user.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)