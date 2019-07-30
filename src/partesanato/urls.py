# partesanato/urls.py

"""partesanato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

from partesanato import views, settings

urlpatterns = [
    path('', views.root),

    path('admin/', admin.site.urls),

    path('auth/password/reset/', RedirectView.as_view(url='/accounts/password/reset/', permanent=True)),
    path('auth/password/reset/confirm/', RedirectView.as_view(url='/accounts/password/reset/', permanent=True)),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),

    path('accounts/', include('allauth.urls')),

    path('', include('posts.urls')),

    path('docs/', get_swagger_view(title='PArtesanato API Docs'), name='docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
