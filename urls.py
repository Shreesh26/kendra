from django.urls import include, path
from . import views
from django.conf import settings
#from django.conf.urld.static import static

urlpatterns = [
    path("search/", views.Search().as_view(), name='search'),
]