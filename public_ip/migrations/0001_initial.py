# Generated by Django 4.2.5 on 2023-09-21 09:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscription', '0002_rename_user_profile_id_subscription_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicIP',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.subscription')),
            ],
        ),
    ]
