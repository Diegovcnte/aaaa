from .models import Usuario, tipoUsuario, Juegos, tipoJuego
from django.forms import ModelForm


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "all"


class tipoForm(ModelForm):
    class Meta:
        model = tipoUsuario
        fields = [
            "tipoUsuario",
        ]
        labels = {
            "tipoUsuario": "tipoUsuario",
        }


class JuegosForm(ModelForm):
    class Meta:
        model = Juegos
        fields = "all"

class tipoJuegosForm(ModelForm):
    class Meta:
        model = tipoJuego
        fields = [
            "tipoJuegos",
        ]
        labels = {
            "tipoJuegos": "tipoJuegos",
        }