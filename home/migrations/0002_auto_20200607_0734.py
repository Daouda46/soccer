# Generated by Django 2.2.10 on 2020-06-07 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipea',
            options={'verbose_name': "L'équipe A", 'verbose_name_plural': 'Equipes A'},
        ),
        migrations.AlterModelOptions(
            name='equipeb',
            options={'verbose_name': "L'équipe B", 'verbose_name_plural': 'Equipes A'},
        ),
    ]
