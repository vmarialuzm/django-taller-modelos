# Generated by Django 4.2.1 on 2023-05-09 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classroom',
            table='classrooms',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teachers',
        ),
    ]
