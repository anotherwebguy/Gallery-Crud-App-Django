# Generated by Django 4.0.6 on 2022-07-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('url', models.CharField(max_length=300)),
                ('detail', models.CharField(max_length=1000)),
            ],
        ),
    ]