# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # <--- This line connects the logout URL
    path('blog/', include('blog.urls')),
    path('', include('pages.urls')),
]