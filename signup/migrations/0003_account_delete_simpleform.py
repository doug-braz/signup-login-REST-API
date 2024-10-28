# Generated by Django 4.2.16 on 2024-10-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_simpleform_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='SimpleForm',
        ),
    ]