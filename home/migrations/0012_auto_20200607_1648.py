# Generated by Django 2.2.10 on 2020-06-07 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_infojoueur_joueur'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Infojoueur',
        ),
        migrations.DeleteModel(
            name='Joueur',
        ),
    ]
