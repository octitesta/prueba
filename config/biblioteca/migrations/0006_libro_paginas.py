# Generated by Django 2.2 on 2020-05-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_libro_codigo_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='paginas',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
