# Generated by Django 3.0.6 on 2020-05-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_authuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='sstudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
