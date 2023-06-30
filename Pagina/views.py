from django.shortcuts import render

# Create your views here.

def boat(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/boat.html", context)


def index(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/index.html", context)
    
def bob(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/bob.html", context)


def flappydino(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/flappydino.html", context)


def foro(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/foro.html", context)


def IniciarSesion(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/IniciarSesion.html", context)


def miner(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/miner.html", context)


def mydreamy(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/mydreamy.html", context)


def pacman(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/pacman.html", context)

def pinpong(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/pingpong.html", context)

def pokedex(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/pokedex.html", context)

def registrar(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/registrar.html", context)

def tazita(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tazita.html", context)

def tetris(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/teris.html", context)

def tipo_add(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tipo_add.html", context)
def tipo_edit(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tipo_edit.html", context)

def tipo_list(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tipo_list.html", context)

def IniciarSesion(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/IniciarSesion.html", context)

def user_add(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/user_add.html", context)

def user_edit(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/user_edit.html", context)

def user_list(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/user_list.html", context)

def tipo_add(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tipo_add.html", context)

def tipo_edit(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tipo_edit.html", context)

def tipo_list(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/tipo_list.html", context)