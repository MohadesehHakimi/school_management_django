from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    student_uid = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    teacher_uid = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.CharField(max_length=50)
    course_uid = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
