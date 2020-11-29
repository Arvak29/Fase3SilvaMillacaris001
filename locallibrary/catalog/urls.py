from django.urls import path
from . import views
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('Store/<int:pk>',views.PlataformGameView.as_view(),name='Store'),
]

urlpatterns+=[
    #Game Views
    path('game/<int:pk>',views.GameDetailView.as_view(),name='game_detail'),
    path('add_game/',views.GameCreate.as_view(),name='add_game'),
    path('game/<int:pk>/update/', views.GameUpdate.as_view(success_url="/"), name='game_update'),
    path('game/<int:pk>/delete/', views.GameDelete.as_view(success_url="/Store/1"), name='game_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)