# Generated by Django 3.0.5 on 2020-05-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]