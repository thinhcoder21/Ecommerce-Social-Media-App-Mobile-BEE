# Generated by Django 5.1.1 on 2024-10-03 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_social_media_app', '0005_alter_postreaction_options_productpostreaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_social_media_app.productpost'),
        ),
    ]
