# Generated by Django 4.0.4 on 2022-05-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion'),
        ),
    ]
