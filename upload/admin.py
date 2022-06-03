from click import File
from django.contrib import admin
from . import models

admin.site.register(models.File)
admin.site.register(models.Area)
admin.site.register(models.Summary)