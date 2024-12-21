from django.contrib import admin
from django.urls import path, include
from escola.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, InstructorViewSet, CourseCategoryViewSet, ModuleCourseViewSet, LessonViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('estudantes', StudentViewSet, basename='Students')
router.register('cursos', CourseViewSet, basename='Courses')
router.register('matriculas', EnrollmentViewSet, basename='Enrollments')
router.register('instrutores', InstructorViewSet, basename='Instructors')
router.register('categorias', CourseCategoryViewSet, basename='Categories')
router.register('modulos', ModuleCourseViewSet, basename='Modules')
router.register('licoes', LessonViewSet, basename='Lessons')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
