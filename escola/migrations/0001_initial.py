# Generated by Django 5.1.4 on 2024-12-21 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CourseCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("bio", models.TextField(max_length=500)),
                ("role", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="instructors"),
                ),
                ("instagram", models.CharField(max_length=100)),
                ("facebook", models.CharField(max_length=100)),
                ("linkedin", models.CharField(max_length=100)),
                ("github", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=500)),
                ("topics", models.TextField(max_length=500)),
                ("video", models.CharField(max_length=10000)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="students"),
                ),
                ("instagram", models.CharField(max_length=100)),
                ("facebook", models.CharField(max_length=100)),
                ("linkedin", models.CharField(max_length=100)),
                ("github", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ModuleCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=500)),
                ("is_active", models.BooleanField(default=True)),
                ("lessons", models.ManyToManyField(to="escola.lesson")),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=500)),
                ("mini_description", models.TextField(max_length=100)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="courses"),
                ),
                ("start_date", models.DateField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.coursecategory",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.instructor",
                    ),
                ),
                (
                    "modules",
                    models.ManyToManyField(
                        related_name="courses", to="escola.modulecourse"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.student"
                    ),
                ),
            ],
        ),
    ]
