# Generated by Django 4.0.5 on 2022-09-19 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=40)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('index', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('balance', models.IntegerField(default=0)),
                ('wallet_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopUp',
            fields=[
                ('ref', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(default=2000)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('payment_time', models.TimeField(auto_now_add=True)),
                ('payment_date_and_time_update', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='BookSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_date', models.DateField(error_messages={'unique': 'Sorry this slot has been booked for this date already.'})),
                ('amount', models.PositiveIntegerField(default=2000)),
                ('ref', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('payment_date_and_time', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('select_plan', models.ForeignKey(default=(('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')), on_delete=django.db.models.deletion.CASCADE, to='book.plan')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.slot')),
            ],
            options={
                'ordering': ('-date_created',),
                'unique_together': {('slot', 'select_date')},
            },
        ),
    ]