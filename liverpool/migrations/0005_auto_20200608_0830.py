# Generated by Django 2.2.10 on 2020-06-08 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liverpool', '0004_auto_20200608_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='infojoueurs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meni', to='liverpool.InfoJoueur'),
        ),
    ]
