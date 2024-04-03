# Generated by Django 5.0.2 on 2024-03-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='ptask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'ptask',
            },
        ),
    ]