# Generated by Django 4.2.5 on 2023-09-21 04:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('user_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile')),
            ],
        ),
    ]
