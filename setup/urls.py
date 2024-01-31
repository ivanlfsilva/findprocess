from django.contrib import admin
from django.urls import path
from process_registers.views import registers

urlpatterns = [path("admin/", admin.site.urls), path("", registers)]
