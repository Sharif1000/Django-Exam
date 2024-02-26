# Generated by Django 5.0.2 on 2024-02-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
        ('taskCategory', '0002_remove_category_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='taskCategory.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assign_date',
            field=models.DateField(),
        ),
    ]
