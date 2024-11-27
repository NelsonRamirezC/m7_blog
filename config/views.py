from django.shortcuts import render
# from django.http import JsonResponse

def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def tema(request, tema):
    contexto = {}
    print("tema: ", tema)
    request.session["tema"]= tema
    return render(request, "index.html", contexto)
    
    # return JsonResponse({"status": "ok"})