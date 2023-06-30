from django.db import models

# Create your models here.
class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(
        primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario')
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def str(self):
        return str(self.tipoUsuario)

class Usuario(models.Model):
    idusuario = models.CharField(max_length=10, primary_key=True)
    nombreUsuario = models.CharField(max_length=50, blank=False, null=False)
    tipoUsuario = models.ForeignKey(
        'tipoUsuario', on_delete=models.CASCADE, db_column='idTipo')
    Correo = models.EmailField(
        unique=True, blank=False, null=False, max_length=100)
    Activo = models.IntegerField()

    def str(self):
        return str(self.nombre)

class Juegos(models.model):
    nombreJuego = models.CharField(max_length=60, blank=False, null=False)
    idJuego = models.CharField(primary_key=True,max_length=50)

    def str(self):
        return str(self.nombreJuego) +" "+str(self.idJuego)