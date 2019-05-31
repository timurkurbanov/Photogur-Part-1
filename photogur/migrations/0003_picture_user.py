# Generated by Django 2.2.1 on 2019-05-31 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photogur', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
