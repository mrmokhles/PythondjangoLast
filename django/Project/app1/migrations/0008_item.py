# Generated by Django 5.0.3 on 2024-04-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
