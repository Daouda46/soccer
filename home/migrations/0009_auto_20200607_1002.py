# Generated by Django 2.2.10 on 2020-06-07 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_equipeb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipeb',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.EquipeA'),
        ),
    ]
