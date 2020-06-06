from django.contrib import admin
from .models import GPS
from .models import Fleet

admin.site.register(GPS)
admin.site.register(Fleet)