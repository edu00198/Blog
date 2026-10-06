from django.contrib import admin
from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha")
    ordering = ("-fecha",)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "post", "contenido", "fecha")
    list_filter = ("fecha", "post")
    search_fields = ("nombre", "contenido")
    ordering = ("-fecha",)