from django.db import models


class Student(models.Model):
    StudentID = models.BigIntegerField(primary_key=True)
    LastName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    Addr1 = models.TextField()
    Addr2 = models.TextField()
    City = models.CharField(max_length=50)
    StateProvince = models.CharField(max_length=10)
    Country = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=20)
    Email = models.EmailField()

    def __str__(self):
        return self.LastName


class Course(models.Model):
    CourseID = models.CharField(primary_key=True, max_length=50)
    CourseName = models.CharField(max_length=100)
    CourseDesc = models.TextField()
    Credits = models.IntegerField()
    DeptID = models.CharField(max_length=10)

    def __str__(self):
        return self.CourseName


class Gradevalue(models.Model):
    Grade = models.CharField(primary_key=True, max_length=50)
    QGrade = models.FloatField(max_length=10)

    def __str__(self):
        return self.QGrade


class Classe(models.Model):
    ClassID = models.BigIntegerField(primary_key=True)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    Term = models.CharField(max_length=50)
    Year = models.BigIntegerField()
    Instructor = models.CharField(max_length=50)
    Classroom = models.CharField(max_length=50)
    ClassTime = models.CharField(max_length=50)

    def __str__(self):
        return self.ClassID


class Stuclasse(models.Model):
    ClassID = models.ForeignKey(Classe, on_delete=models.CASCADE)
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Grade = models.ForeignKey(Gradevalue, on_delete=models.CASCADE)
