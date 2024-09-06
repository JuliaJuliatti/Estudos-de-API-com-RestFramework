from django.db import models

# Create your models here.

'''no django models é para criar uma tabela ou seja os dados que eu vou extrair na minh aplição, django.db (data base), existem diferentes tipos de dados, como por exemplo strings, inteiros)
para isso quando eu crio o os dados eu utilizo diferentes classificações ex: CharField para titulos curtos, '''

class Filmes(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    classif = models.CharField(max_length=255)


# quando modificamos o banco de dados ele nao atualiza aqui, pois está rodando paralelo

class Genero(models.Model):
    genero = models.CharField(max_length=255)


