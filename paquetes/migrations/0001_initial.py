# Generated by Django 2.2.4 on 2019-08-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.PositiveIntegerField()),
                ('gia', models.CharField(max_length=100)),
                ('fechaPartida', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=500)),
            ],
        ),
    ]
