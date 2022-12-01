# Generated by Django 4.0.6 on 2022-11-10 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_rename_text_vocabulary_word_remove_vocabulary_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='word',
        ),
        migrations.AlterField(
            model_name='sentence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ali', to=settings.AUTH_USER_MODEL),
        ),
    ]
