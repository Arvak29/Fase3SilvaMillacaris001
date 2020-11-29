from django.urls import path
from . import views
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    #path('settings/<str:username>', views.settings, name='settings'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)