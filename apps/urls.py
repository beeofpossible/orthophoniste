from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name=''
urlpatterns = [
    path('', views.media_list, name='media_list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)