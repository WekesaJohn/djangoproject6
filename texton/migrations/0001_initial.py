# Generated by Django 4.2 on 2023-04-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]