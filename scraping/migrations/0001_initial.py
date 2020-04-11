# Generated by Django 3.0.5 on 2020-04-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('position', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'active'), ('archive', 'archive')], max_length=7)),
                ('description', models.TextField()),
            ],
        ),
    ]