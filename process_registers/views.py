from django.shortcuts import render
from django.http import HttpResponse

def registers(request):
    return render(request, "process_registers/process_registers.html")