# Generated by Django 3.2.7 on 2021-09-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('area', models.IntegerField()),
                ('capital', models.TextField()),
                ('independence', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]