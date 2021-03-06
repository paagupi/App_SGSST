# Generated by Django 3.2.7 on 2021-11-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ausentismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=20, null=True, verbose_name='Periodo')),
                ('salario_dia', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Salario día')),
                ('origen_incapacidad', models.CharField(blank=True, choices=[('Enfermedad laboral', 'Enfermedad laboral'), ('Accidente de trabajo', 'Accidente de trabajo')], max_length=20, null=True, verbose_name='Origen de la incapacidad')),
                ('codigo_enfermedad', models.CharField(max_length=15, verbose_name='Codigo de la enfermedad')),
                ('diagnostico', models.CharField(max_length=250, verbose_name='Diagnostico')),
                ('grupo_dx', models.CharField(max_length=100, verbose_name='Grupo DX')),
                ('segmento_osteomuscular', models.CharField(max_length=100, verbose_name='Segmento Osteomuscular')),
                ('origen', models.CharField(max_length=50, verbose_name='Origen de la enfermedad')),
                ('clasificacion', models.CharField(blank=True, choices=[('Inicial', 'Inicial'), ('Prórroga', 'Prórroga')], max_length=30, null=True, verbose_name='Origen de la incapacidad')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de de inicio')),
                ('fecha_finalizacion', models.DateField(verbose_name='Fecha de finalizacion')),
                ('total_incapacidad', models.CharField(max_length=5, verbose_name='Total dias de incapacidad')),
                ('valor_incapacidad', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor incapacidad')),
                ('valor_asumido_empresa', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor asumido por la empresa')),
                ('Valor_asumido_eps', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor asumido por la eps')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('nombre_completo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empleados')),
            ],
            options={
                'verbose_name': 'Ausentismo',
            },
        ),
    ]
