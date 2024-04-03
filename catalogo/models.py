from django.db import models
# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    resumo = models.TextField()

    def __str__(self):
        return self.titulo
