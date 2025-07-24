from django.db import migrations

def agregar_categorias(apps, schema_editor):
    Categoria = apps.get_model('productos', 'Categoria')
    categorias = [
        'Frutas',
        'Verduras',
        'Limpieza',
        'Lácteos',
        'Bebidas',
    ]
    for nombre in categorias:
        Categoria.objects.get_or_create(nombre=nombre)

class Migration(migrations.Migration):
    dependencies = [
        ('productos', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(agregar_categorias),
    ] 