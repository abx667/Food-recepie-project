# Generated by Django 5.2 on 2025-04-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_description', models.TextField()),
                ('receipe_name', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
