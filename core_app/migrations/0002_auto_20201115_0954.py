# Generated by Django 3.1.3 on 2020-11-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='question_list',
        ),
        migrations.AddField(
            model_name='quiz',
            name='question_list',
            field=models.ManyToManyField(blank=True, to='core_app.Question'),
        ),
    ]
