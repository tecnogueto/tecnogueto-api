from escola.models import Student, Course, Enrollment, Instructor, CourseCategory, ModuleCourse, Lesson
from django.contrib import admin
from image_cropping import ImageCroppingMixin

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20

admin.site.register(Course, CourseAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'student', 'start_date', 'end_date')
    list_display_links = ('id', 'course')
    search_fields = ('course',)
    list_per_page = 20

admin.site.register(Enrollment, EnrollmentAdmin)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Instructor, InstructorAdmin)

class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(CourseCategory, CourseCategoryAdmin)

class ModuleCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20

admin.site.register(ModuleCourse, ModuleCourseAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'topics', 'video', 'is_active')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20

admin.site.register(Lesson, LessonAdmin)

class InstructorAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'image')