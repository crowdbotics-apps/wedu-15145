# Generated by Django 2.2.11 on 2020-03-28 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_id', models.BigIntegerField()),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('jobtitle', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]