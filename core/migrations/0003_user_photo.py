# Generated by Django 3.2 on 2021-04-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_answer_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="photo",
            field=models.ImageField(
                default="sample.jpg", upload_to="user_profile_photos"
            ),
            preserve_default=False,
        ),
    ]
