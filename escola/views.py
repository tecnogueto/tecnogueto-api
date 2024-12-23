from escola.models import Student, Course, Enrollment, Instructor, CourseCategory, ModuleCourse, Lesson
from escola.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, InstructorSerializer, CourseCategorySerializer, ModuleCourseSerializer, LessonSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

class ModuleCourseViewSet(viewsets.ModelViewSet):
    queryset = ModuleCourse.objects.all()
    serializer_class = ModuleCourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


