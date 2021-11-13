# Generated by Django 3.2.6 on 2021-11-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_capacitaciones_detallesanidad_sanidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallesanidad',
            options={'verbose_name': 'Sanidad - Detalle tratamiento', 'verbose_name_plural': 'Sanidad - Detalle tratamientos'},
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresa'},
        ),
        migrations.AlterModelOptions(
            name='sanidad',
            options={'verbose_name': 'Sanidad (COVID-19 u otras)', 'verbose_name_plural': 'Sanidad (COVID-19 u otras)'},
        ),
        migrations.AlterModelOptions(
            name='tipoempresa',
            options={'verbose_name': 'Tipo de empresa', 'verbose_name_plural': 'Tipo de empresa'},
        ),
        migrations.AddField(
            model_name='areas',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='areas',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AddField(
            model_name='capacitaciones',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='capacitaciones',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AddField(
            model_name='cargos',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='cargos',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AddField(
            model_name='empleados',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='empleados',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AddField(
            model_name='nivelacademico',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='nivelacademico',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AddField(
            model_name='tipoempresa',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='tipoempresa',
            name='modify_at',
            field=models.DateField(auto_now=True, verbose_name='Actualizado el'),
        ),
        migrations.AlterField(
            model_name='detallesanidad',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AlterField(
            model_name='sanidad',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
    ]
