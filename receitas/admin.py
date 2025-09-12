from django.contrib import admin
from .models import Receita

# Register your models here.
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoria', 'created_at', 'updated_at', 'image_preview')
    list_filter = ('categoria', 'created_at')
    search_fields = ('title', 'description', 'ingredients')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 200px;"/>'
        return "Sem imagem"
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview da Imagem'
