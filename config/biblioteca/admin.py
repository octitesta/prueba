from django.contrib import admin

# Register your models here.
from. models import *

class UsuarioAdmin(admin.ModelAdmin):
    #exclude = ['codigo', 'telefono']
    fieldsets = (
        ('Datos', {
            'fields': ('nombre',)
        }),
        ('Contacto', {
            'fields': ('telefono','direccion')
        }),
    )
    list_display = ['nombre', 'telefono', 'direccion']
    

class EjemplarAdmin(admin.ModelAdmin):
    list_filter = ['libro',]
    

class LibroAdmin(admin.ModelAdmin):
    #filter_vertical = ('titulo',)
    list_display = ['titulo', 'editorial',]
    

class LibroInline(admin.TabularInline):
    model = Libro

class AutorAdmin(admin.ModelAdmin):
    #list_display = []
    inlines = [LibroInline,]
    
    search_fields = ['nombre','libro__titulo','libro__editorial']


admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Ejemplar,EjemplarAdmin)
admin.site.register(Usuario, UsuarioAdmin)
