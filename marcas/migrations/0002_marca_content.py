# Generated by Django 4.1.3 on 2022-11-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marcas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='content',
            field=models.TextField(null=True),
        ),
    ]