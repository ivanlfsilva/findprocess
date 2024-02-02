from django.shortcuts import render


def process_registers(request):

    nome = "ivan luis"
    alunos = ["ivan luis", "mariah luysa" , "yan nicolas", "fabiana"]
    return render(request, "process_registers/process_registers.html", {"nome": nome , "alunos": alunos})
