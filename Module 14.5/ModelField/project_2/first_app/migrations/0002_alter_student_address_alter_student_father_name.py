# Generated by Django 5.0.2 on 2024-02-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='Rahim', max_length=30),
        ),
    ]
