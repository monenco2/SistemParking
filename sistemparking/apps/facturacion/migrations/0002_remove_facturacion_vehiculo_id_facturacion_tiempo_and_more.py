# Generated by Django 5.2.3 on 2025-06-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturacion',
            name='vehiculo_id',
        ),
        migrations.AddField(
            model_name='facturacion',
            name='tiempo',
            field=models.TextField(blank=True, verbose_name='tiempo'),
        ),
        migrations.AddField(
            model_name='facturacion',
            name='vehiculo',
            field=models.TextField(blank=True, verbose_name='vehiculo'),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='metodo_pago',
            field=models.TextField(blank=True, verbose_name='pago'),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='valor_pagar',
            field=models.TextField(null=True, verbose_name='valor'),
        ),
    ]
