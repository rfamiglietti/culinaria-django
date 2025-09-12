from django.db import models

# Create your models here.
class Receita(models.Model):
    CATEGORIAS = [
        ('comida', 'Comida'),
        ('sobremesa', 'Sobremesa'),
        ('drink', 'Drink'),
    ]
    
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    ingredients = models.TextField('Ingredientes')
    instructions = models.TextField('Modo de Preparo')
    
    image = models.ImageField(upload_to='receitas/images/', null=True, blank=True)
   
    categoria = models.CharField('Categoria', max_length=50, choices=CATEGORIAS, default='comida')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-created_at'] #ordena as receitas da mais nova para a mais antiga