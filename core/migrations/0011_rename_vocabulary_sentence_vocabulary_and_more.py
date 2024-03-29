# Generated by Django 4.0.6 on 2022-11-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_word_id_alter_word_vocabulary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentence',
            old_name='Vocabulary',
            new_name='vocabulary',
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='translation',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='word',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
