# Generated by Django 4.0.6 on 2022-07-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_vocabulary_name_vocabulary_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='review_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
