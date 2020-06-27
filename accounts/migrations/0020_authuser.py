# Generated by Django 3.0.6 on 2020-05-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200426_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=30, unique=True)),
                ('email', models.TextField(max_length=254, unique=True)),
                ('password', models.TextField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
    ]
