from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Student, Teacher, Course
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer


class TeacherApiView(APIView):

    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Teacher created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailApiView(APIView):

    def get(self, request, teacher_uid, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(teacher_uid=teacher_uid)
        except Teacher.DoesNotExist:
            return Response({'message': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, teacher_uid, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(teacher_uid=teacher_uid)
        except Teacher.DoesNotExist:
            return Response({'message': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Teacher updated successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, teacher_uid, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(teacher_uid=teacher_uid)
        except Teacher.DoesNotExist:
            return Response({'message': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return Response({'message': 'Teacher deleted successfully'}, status=status.HTTP_200_OK)


class StudentApiView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailApiView(APIView):
    def get(self, request, student_uid, *args, **kwargs):
        try:
            student = Student.objects.get(student_uid=student_uid)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, student_uid, *args, **kwargs):
        try:
            student = Student.objects.get(student_uid=student_uid)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student updated successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_uid, *args, **kwargs):
        try:
            student = Student.objects.get(student_uid=student_uid)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({'message': 'Student deleted successfully'}, status=status.HTTP_200_OK)


# find the type of the object by its uid
class FindUserTypeByUid(APIView):
    def get(self, request, uid, *args, **kwargs):
        try:
            student = Student.objects.get(student_uid=uid)
            return Response({'type': 'student'}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            try:
                teacher = Teacher.objects.get(teacher_uid=uid)
                return Response({'type': 'teacher'}, status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                pass

        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class CourseApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Course created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, course_uid, *args, **kwargs):
        try:
            course = Course.objects.get(course_uid=course_uid)
        except Course.DoesNotExist:
            return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, course_uid, *args, **kwargs):
        try:
            course = Course.objects.get(course_uid=course_uid)
        except Course.DoesNotExist:
            return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Course updated successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_uid, *args, **kwargs):
        try:
            course = Course.objects.get(course_uid=course_uid)
        except Course.DoesNotExist:
            return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        course.delete()
        return Response({'message': 'Course deleted successfully'}, status=status.HTTP_200_OK)
