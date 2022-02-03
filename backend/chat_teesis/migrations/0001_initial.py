# Generated by Django 3.1.14 on 2022-02-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentee_question_col',
            fields=[
                ('mentee_question_Id', models.AutoField(primary_key=True, serialize=False)),
                ('thesis_plan_Id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('mentee_question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mentor_answer_col',
            fields=[
                ('mentor_answer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('mentor_answer', models.TextField()),
                ('mentee_question_Id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('user_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='thesis_plan_col',
            fields=[
                ('thesis_plan_Id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=128)),
                ('schedule', models.IntegerField()),
                ('on_domestic', models.BooleanField()),
                ('journal_tier', models.BooleanField()),
                ('purpose', models.CharField(max_length=32)),
                ('user_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_col',
            fields=[
                ('user_Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='신규 회원', max_length=64)),
                ('major', models.CharField(blank=True, max_length=128)),
                ('degree', models.CharField(blank=True, max_length=16)),
                ('contact_email', models.CharField(blank=True, max_length=32)),
                ('belong', models.CharField(blank=True, max_length=64)),
                ('career', models.CharField(blank=True, max_length=128)),
                ('img_link', models.SlugField(blank=True, max_length=128)),
            ],
        ),
    ]
