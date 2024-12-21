from rest_framework import serializers
from escola.models import Student, Course, Enrollment, Instructor, CourseCategory, ModuleCourse, Lesson

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ModuleCourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    class Meta:
        model = ModuleCourse
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    category = CourseCategorySerializer()
    modules = ModuleCourseSerializer(many=True)  
    class Meta:
        model = Course
        fields = '__all__'