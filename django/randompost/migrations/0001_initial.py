# Generated by Django 2.1.4 on 2018-12-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=20)),
                ('second', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]