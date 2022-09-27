# Generated by Django 3.1.7 on 2021-03-17 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museum', '0002_booking_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='uname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking_details',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
