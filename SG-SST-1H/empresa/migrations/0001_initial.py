# Generated by Django 3.2.6 on 2021-10-23 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=150, verbose_name='Números telefónicos')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=150, verbose_name='Tipo de empresa')),
            ],
            options={
                'verbose_name': 'Tipo de empresa',
                'verbose_name_plural': 'Tipo de empresas',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256, verbose_name='Nombre de la empresa')),
                ('nit', models.CharField(max_length=25, verbose_name='Número de identificación tributaria')),
                ('actividad_economica', models.CharField(max_length=50, verbose_name='Actividad económica')),
                ('nivel_de_riesgo', models.CharField(max_length=10, verbose_name='Nivel de riesgo')),
                ('naturaleza_juridica', models.CharField(max_length=50, verbose_name='Naturaleza jurídica')),
                ('correo_electronico', models.CharField(max_length=25, verbose_name='Correo electrónico')),
                ('tipo_de_empresa', models.CharField(max_length=25, verbose_name='Tipo de empresa')),
                ('numeros_telefonicos', models.CharField(max_length=40, verbose_name='Números telefónicos')),
                ('tipo_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empresa.tipoempresa')),
            ],
            options={
                'verbose_name': 'Empresa',
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empleado', models.CharField(max_length=30, null=True, verbose_name='ID empleado')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('cargo', models.CharField(max_length=30, verbose_name='Cargo del empleado')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Sueldo')),
                ('nivel', models.CharField(max_length=40, verbose_name='Nivel')),
                ('eps', models.CharField(max_length=100, verbose_name='EPS')),
                ('arl', models.CharField(max_length=100, verbose_name='ARL')),
                ('cuenta_bancaria', models.CharField(max_length=30, null=True, verbose_name='Número de cuenta bancaria')),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empresa.areas')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.AddField(
            model_name='areas',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
