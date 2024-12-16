# Generated by Django 4.2.17 on 2024-12-16 11:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DisabledTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.TimeField(choices=[(datetime.time(8, 0), '08:00'), (datetime.time(10, 0), '10:00'), (datetime.time(12, 0), '12:00'), (datetime.time(14, 0), '14:00'), (datetime.time(16, 0), '16:00')])),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'unique_together': {('date', 'time_slot')},
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.TimeField(choices=[(datetime.time(8, 0), '08:00'), (datetime.time(10, 0), '10:00'), (datetime.time(12, 0), '12:00'), (datetime.time(14, 0), '14:00'), (datetime.time(16, 0), '16:00')])),
                ('is_canceled', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('date', 'time_slot')},
            },
        ),
    ]