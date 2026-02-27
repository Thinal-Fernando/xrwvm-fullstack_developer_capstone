from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'djangoapp'
urlpatterns = [
    path(route='get_cars', view=views.get_cars, name ='getcars'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
