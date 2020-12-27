from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.all, name="home"),
    path('<slug:slug>/' , views.find_post, name='find_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)