# Generated by Django 2.1.7 on 2019-03-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipaments', '0002_auto_20190321_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='Equipamento',
            new_name='caixa',
        ),
        migrations.AlterField(
            model_name='equipaments',
            name='location',
            field=models.TextField(verbose_name='Endereço'),
        ),
    ]
