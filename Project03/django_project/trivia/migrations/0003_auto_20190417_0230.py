# Generated by Django 2.2 on 2019-04-17 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20190417_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='info', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
