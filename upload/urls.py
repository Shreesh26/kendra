from django.urls import include, path
from . import views
from django.conf import settings
#from django.conf.urld.static import static

urlpatterns = [
    path("upload/", views.Upload().as_view(), name="upload_docs"),
    
]