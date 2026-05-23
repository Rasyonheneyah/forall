from django.db import models

from django.contrib.auth.models import AbstractUser 

class Cursos():
    nome = models.CharField('Curso', max_lenght=200)

    def __str__(self):
        return self.nome

class User(AbstarctUser):
    nome = models.CharField('Nome', max_lenght=200)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name='Curso')
    email = models.EmailField('Email',)
    bio = 0

    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("Modificado em", auto_now=True)
