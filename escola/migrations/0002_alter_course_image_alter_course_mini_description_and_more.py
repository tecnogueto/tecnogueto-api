# Generated by Django 5.1.4 on 2024-12-22 13:44

import escola.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("escola", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="courses",
                validators=[escola.models.validate_svg],
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="mini_description",
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name="instructor",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="instructors"),
        ),
    ]