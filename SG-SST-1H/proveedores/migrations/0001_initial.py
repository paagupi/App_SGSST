# Generated by Django 3.2.7 on 2021-11-20 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleElementos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proveedor', models.CharField(max_length=30, null=True, verbose_name='ID proveedor')),
                ('id_elemento', models.CharField(max_length=30, null=True, verbose_name='ID elemento')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripción del elemento')),
                ('vida_util', models.CharField(max_length=30, null=True, verbose_name='Vida útil')),
                ('activo', models.BooleanField(default=False, verbose_name='Se encuentra activo?')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creación')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Detalle elememto',
                'verbose_name_plural': 'Detalle elementos',
            },
        ),
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_elemento', models.CharField(max_length=30, null=True, verbose_name='ID elemento')),
                ('nombre_elemento', models.CharField(max_length=100, verbose_name='Nombre del elemento')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creación')),
                ('activo', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2, verbose_name='Se encuentra activo?')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Elemento',
                'verbose_name_plural': 'Elementos',
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100, verbose_name='Nombre de la empresa')),
                ('nit', models.CharField(max_length=25, verbose_name='Número de identificación tributaria')),
                ('id_proveedor', models.CharField(max_length=30, null=True, verbose_name='ID proveedor')),
                ('certificado_arl', models.CharField(max_length=50, verbose_name='ARL')),
                ('es_autorizado', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2, verbose_name='Se encuentra autorizado?')),
                ('seguridad_social', models.CharField(max_length=50, verbose_name='EPS')),
                ('ficha_seguridad_social', models.CharField(max_length=256, verbose_name='Ficha seguridad social')),
                ('telefono1', models.CharField(max_length=40, verbose_name='Número telefónico 1')),
                ('telefono2', models.CharField(max_length=40, verbose_name='Número telefónico 2')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('activo', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2, verbose_name='Se encuentra activo?')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creación')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('tipo_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empresa.tipoempresa')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
