from rest_framework import serializers
from .models import Filmes

'''serializers vai entender a tabela e converter para JSON'''

class FilmesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['id', 'titulo', 'genero', 'ano', 'idioma', 'classif']


