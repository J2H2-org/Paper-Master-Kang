# Generated by Django 3.1.14 on 2022-01-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatphone_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('selled', models.BooleanField(default=False)),
            ],
        ),
    ]
