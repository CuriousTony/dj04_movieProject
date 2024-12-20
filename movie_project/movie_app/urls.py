from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('about/', views.about, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
