# Generated by Django 2.1.4 on 2019-01-03 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_auto_20181227_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
