from django.contrib import admin
from django.urls import path

from process_registers.views import process_registers

urlpatterns = [path("admin/", admin.site.urls), path("", process_registers)]
