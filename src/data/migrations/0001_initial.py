# Generated by Django 3.0.5 on 2020-04-14 22:14

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
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Descripción')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de fin')),
                ('enabled', models.BooleanField(default=True, verbose_name='¿Esta habilitado?')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_result_i', models.IntegerField(verbose_name='Resultado del riesgo infección')),
                ('risk_result_v', models.IntegerField(verbose_name='Resultado del riesgo vulnerabilidad')),
                ('validity', models.DateTimeField(verbose_name='Fecha validez')),
                ('completion_date', models.DateTimeField(verbose_name='Fecha completado')),
                ('enabled', models.BooleanField(default=True, verbose_name='¿Esta habilitado?')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='data.Survey', verbose_name='Encuesta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
                'ordering': ('-completion_date',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Orden')),
                ('text', models.CharField(max_length=300, verbose_name='Texto')),
                ('question_type', models.CharField(choices=[(1, 'Uníca'), (2, 'Selección multiple'), (3, 'Numerica')], default=1, max_length=200, verbose_name='Tipo')),
                ('enabled', models.BooleanField(default=True, verbose_name='¿Esta habilitado?')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='data.Survey', verbose_name='Encuesta')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
                'ordering': ('survey', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Orden')),
                ('text', models.CharField(max_length=300, verbose_name='Texto')),
                ('risk_value_infection', models.IntegerField(verbose_name='Valor de riesgo infección')),
                ('risk_value_vulnerability', models.IntegerField(verbose_name='Valor de riesgo vulnerabilidad')),
                ('enabled', models.BooleanField(default=True, verbose_name='¿Esta habilitado?')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='data.Question', verbose_name='Pregunta')),
            ],
            options={
                'verbose_name': 'Opción',
                'verbose_name_plural': 'Opciones',
                'ordering': ('question', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='Valor')),
                ('risk_result_i', models.IntegerField(verbose_name='Resultado del riesgo infección')),
                ('risk_result_v', models.IntegerField(verbose_name='Resultado del riesgo vulnerabilidad')),
                ('enabled', models.BooleanField(default=True, verbose_name='¿Esta habilitado?')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('option', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='data.Option', verbose_name='Opción')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='data.Response', verbose_name='Respuesta')),
            ],
            options={
                'verbose_name': 'Opcion respondida',
                'verbose_name_plural': 'Opciones respondidas',
                'ordering': ('response', 'id'),
            },
        ),
    ]
