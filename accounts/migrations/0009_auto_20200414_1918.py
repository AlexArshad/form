# Generated by Django 3.0.4 on 2020-04-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200414_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='form',
        ),
    ]
