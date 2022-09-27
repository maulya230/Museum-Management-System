# Generated by Django 3.1.7 on 2021-03-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
            ],
        ),
    ]