# Generated by Django 3.1.7 on 2021-03-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_notes_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(max_length=259),
        ),
    ]
