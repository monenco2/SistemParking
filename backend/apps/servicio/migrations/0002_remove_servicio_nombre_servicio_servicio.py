# Generated by Django 5.2.3 on 2025-07-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='nombre',
        ),
        migrations.AddField(
            model_name='servicio',
            name='servicio',
            field=models.TextField(null=True, verbose_name='servicio'),
        ),
    ]
