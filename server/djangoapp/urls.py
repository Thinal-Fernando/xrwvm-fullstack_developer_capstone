from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'djangoapp'
urlpatterns = [
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path(route='login', view=views.login_user, name='login'),
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealerships'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='add_review', view=views.add_review, name='add_review'),








] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
