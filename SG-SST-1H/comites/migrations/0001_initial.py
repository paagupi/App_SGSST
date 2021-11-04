# Generated by Django 3.2.7 on 2021-11-04 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0002_auto_20211025_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comite', models.CharField(max_length=60, verbose_name='Nombre de Comite')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Comite',
                'verbose_name_plural': 'Comites',
            },
        ),
        migrations.CreateModel(
            name='RolComite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_comite', models.CharField(max_length=50, verbose_name='Rol Comite')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Rol comite',
                'verbose_name_plural': 'Roles comite',
            },
        ),
        migrations.CreateModel(
            name='ParticipanteComite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_comite', models.CharField(max_length=50, verbose_name='Rol Comite')),
                ('participantes_comite', models.CharField(max_length=60, verbose_name='Participante comite')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cargos')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empleados')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
            },
        ),
    ]