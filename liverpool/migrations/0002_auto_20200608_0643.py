# Generated by Django 2.2.10 on 2020-06-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liverpool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='origincoach',
            name='photo',
            field=models.ImageField(blank='True', null='True', upload_to='liverpool/photo'),
        ),
    ]
