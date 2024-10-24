"""
URL configuration for casher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from wechat_django.sites import wechat

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path("wechat/", wechat.urls),
    path("flow/", include("flow.urls")),
    path("task/", include("task.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("rest-auth/", include("dj_rest_auth.urls")),
    path("auth/accounts/", include("allauth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
