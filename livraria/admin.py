from django.contrib import admin

from livraria.models import Autor, Categoria, Editora, Livro

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)

# Register your models here.
