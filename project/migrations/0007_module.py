# Generated by Django 5.0.2 on 2024-03-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_usertask'),
    ]

    operations = [
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'module',
            },
        ),
    ]
