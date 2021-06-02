# Generated by Django 3.2.3 on 2021-06-01 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('cartera', models.FloatField(default=1000000)),
                ('bitcoin', models.FloatField(default=0)),
                ('binance', models.FloatField(default=0)),
                ('ethereum', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=150)),
            ],
        ),
    ]
