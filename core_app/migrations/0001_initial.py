# Generated by Django 3.1.3 on 2020-11-15 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TimeStamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('timestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.timestamp')),
                ('question_text', models.CharField(blank=True, max_length=200, null=True)),
            ],
            bases=('core_app.timestamp',),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('timestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.timestamp')),
                ('name', models.CharField(max_length=200)),
                ('question_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='core_app.question')),
            ],
            bases=('core_app.timestamp',),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_selected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_quiz_score', to='core_app.quizscore')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='quizscore',
            name='quiz_attended',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_quiz', to='core_app.quiz'),
        ),
        migrations.CreateModel(
            name='OptionList',
            fields=[
                ('timestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.timestamp')),
                ('choice_text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question_text', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.question')),
            ],
            bases=('core_app.timestamp',),
        ),
    ]
