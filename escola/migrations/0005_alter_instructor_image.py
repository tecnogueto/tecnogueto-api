# Generated by Django 5.1.4 on 2024-12-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("escola", "0004_instructor_cropping_alter_instructor_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instructor",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="instructors/images"
            ),
        ),
    ]
