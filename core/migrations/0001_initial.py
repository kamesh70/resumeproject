# Generated by Django 3.0.5 on 2020-05-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('emailin', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('textmes', models.CharField(max_length=500)),
            ],
        ),
    ]
