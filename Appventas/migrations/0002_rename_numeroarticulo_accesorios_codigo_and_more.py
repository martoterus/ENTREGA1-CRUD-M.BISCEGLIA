# Generated by Django 4.0.6 on 2022-08-12 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesorios',
            old_name='numeroArticulo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='bicicletas',
            old_name='numeroArticulo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='indumentaria',
            old_name='numeroArticulo',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='repuestos',
            old_name='numeroArticulo',
            new_name='codigo',
        ),
    ]