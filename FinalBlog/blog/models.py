from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    visible = models.CharField(max_length=10, default=' ')
    image = models.ImageField(upload_to="imagblog", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Contacto(models.Model):    
    nombreApellido= models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mensaje= models.TextField()