from django.db import models
from django.utils.text import slugify
import os
from django.core.exceptions import ValidationError
from image_cropping import ImageRatioField

def validate_svg(value):
    ext = os.path.splitext(value.name)[1]
    if ext.lower() != '.svg':
        raise ValidationError('Apenas arquivos SVG são permitidos.')

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField(max_length=500)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='instructors', blank=True, null=True)
    cropping = ImageRatioField('image', '300x300')
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ModuleCourse(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    lessons = models.ManyToManyField('Lesson')

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    mini_description = models.TextField(max_length=250)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    image = models.FileField(upload_to='courses', blank=True, null=True, validators=[validate_svg])
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    modules = models.ManyToManyField(ModuleCourse, related_name='courses')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    topics = models.TextField(max_length=500)
    video = models.CharField(max_length=10000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Enrollment in {self.course.title}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='students', blank=True, null=True)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    def __str__(self):
        return self.name