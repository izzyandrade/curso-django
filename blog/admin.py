from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nome', 'publicado', 'criado',)
    list_filter = ('nome', 'publicado', 'criado',)
    date_hierarchy = 'publicado'
    search_fields = ('nome',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    date_hierarchy = 'publicado'
    readonly_fields = ('visualizar_imagem',)
    raw_id_fields = ('autor',)
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)}

    def visualizar_imagem(self, obj):
        return obj.view_image

    visualizar_imagem.short_description = "Imagem Cadastrada"

# Register your models here.
