# Generated by Django 4.0.2 on 2022-07-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('media', models.CharField(max_length=100)),
            ],
        ),
    ]
