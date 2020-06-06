
from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("id", views.id_json),
    path("fleet/<num>", views.fleet)
]
