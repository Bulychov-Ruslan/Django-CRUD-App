from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    sql='''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    student_list = Student.objects.all().order_by('FirstName')
    context = {
        'student_list': student_list,
        'students': stud
    }
    return render(request, 'index.html', context)


def add_student(request):
    if request.method == "POST":
        StudentID = request.POST['StudentID']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        MiddleName = request.POST['MiddleName']
        Addr1 = request.POST['Addr1']
        Addr2 = request.POST['Addr2']
        City = request.POST['City']
        StateProvince = request.POST['StateProvince']
        Country = request.POST['Country']
        PostalCode = request.POST['PostalCode']
        Email = request.POST['Email']
        student = Student(StudentID=StudentID, FirstName=FirstName, LastName=LastName, MiddleName=MiddleName, Addr1=Addr1, Addr2=Addr2, City=City, StateProvince=StateProvince, Country=Country, PostalCode=PostalCode, Email=Email)
        messages.info(request, "Insert success!!!")
        student.save()
    else:
        pass

    sql='''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    student_list = Student.objects.all().order_by('FirstName')
    context = {
        'student_list': student_list,
        'students': stud
    }
    return render(request, 'index.html', context)


def delete_student(request, myid):
    student1 = Student.objects.get(StudentID = myid)
    student1.delete()
    messages.info(request, "Delete success!!!")
    return redirect(index)


def edit_student(request, myid):
    student2 = Student.objects.get(StudentID = myid)
    student_list = Student.objects.all().order_by('FirstName')
    sql = '''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    context = {
        'student2': student2,
        'student_list': student_list,
        'students': stud
    }
    return render(request, 'index.html', context)


def update_student(request, myid):
    student = Student.objects.get(StudentID = myid)
    student.StudentID = request.POST['StudentID']
    student.FirstName = request.POST['FirstName']
    student.LastName = request.POST['LastName']
    student.MiddleName = request.POST['MiddleName']
    student.Addr1 = request.POST['Addr1']
    student.Addr2 = request.POST['Addr2']
    student.City = request.POST['City']
    student.StateProvince = request.POST['StateProvince']
    student.Country = request.POST['Country']
    student.PostalCode = request.POST['PostalCode']
    student.Email = request.POST['Email']
    student.save()
    messages.info(request, "Update success!!!")
    return redirect(index)

###################################################################################################################
def classes(request):
    sql = '''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    classes_list = Classe.objects.all()
    context = {
        'classes_list': classes_list,
        'students': stud
    }
    return render(request, 'classes.html', context)


def add_classes(request):
    if request.method == "POST":
        ClassID = request.POST['ClassID']
        Term = request.POST['Term']
        Year = request.POST['Year']
        Instructor = request.POST['Instructor']
        Classroom = request.POST['Classroom']
        ClassTime = request.POST['ClassTime']
        CourseID_id = request.POST['CourseID_id']
        classes = Classe(ClassID=ClassID, Term=Term, Year=Year, Instructor=Instructor, Classroom=Classroom, ClassTime=ClassTime, CourseID_id=CourseID_id)
        messages.info(request, "Insert success!!!")
        classes.save()
    else:
        pass

    sql='''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    classes_list = Classe.objects.all()
    context = {
        'classes_list': classes_list,
        'students': stud
    }
    return render(request, 'classes.html', context)


def delete_classes(request, myid):
    classes1 = Classe.objects.get(ClassID = myid)
    classes1.delete()
    messages.info(request, "Delete success!!!")
    return redirect(classes)


def edit_classes(request, myid):
    sql = '''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    classes2 = Classe.objects.get(ClassID = myid)
    classes_list = Classe.objects.all()
    context = {
        'classes2': classes2,
        'classes_list': classes_list,
        'students': stud
    }
    return render(request, 'classes.html', context)


def update_classes(request, myid):
    classess = Classe.objects.get(ClassID = myid)
    classess.ClassID = request.POST['ClassID']
    classess.Term = request.POST['Term']
    classess.Year = request.POST['Year']
    classess.Instructor = request.POST['Instructor']
    classess.Classroom = request.POST['Classroom']
    classess.ClassTime = request.POST['ClassTime']
    classess.CourseID_id = request.POST['CourseID_id']
    classess.save()
    messages.info(request, "Update success!!!")
    return redirect(classes)

# ###################################################################################################################
def stuclasses(request):
    sql = '''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    stuclasses_list = Stuclasse.objects.all()
    context = {
        'stuclasses_list': stuclasses_list,
        'students': stud
    }
    return render(request, 'stuclasses.html', context)


def add_stuclasses(request):
    if request.method == "POST":
        ClassID_id = request.POST['ClassID_id']
        Grade_id = request.POST['Grade_id']
        StudentID_id = request.POST['StudentID_id']
        stuclasses = Stuclasse(ClassID_id=ClassID_id, Grade_id=Grade_id, StudentID_id=StudentID_id)
        messages.info(request, "Insert success!!!")
        stuclasses.save()
    else:
        pass

    sql = '''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    stuclasses_list = Stuclasse.objects.all()
    context = {
        'stuclasses_list': stuclasses_list,
        'students': stud
    }
    return render(request, 'stuclasses.html', context)


def delete_stuclasses(request, myid):
    stuclasses1 = Stuclasse.objects.get(id = myid)
    stuclasses1.delete()
    messages.info(request, "Delete success!!!")
    return redirect(stuclasses)


def edit_stuclasses(request, myid):
    sql = '''SELECT * FROM "main_student" as s JOIN "main_stuclasse" as stu ON stu."StudentID_id" = s."StudentID" JOIN "main_classe" as cl ON cl."ClassID" = stu."ClassID_id" JOIN "main_course" as co ON co."CourseID" = cl."CourseID_id" order by s."FirstName"'''
    stud = Student.objects.raw(sql)
    stuclasses2 = Stuclasse.objects.get(id = myid)
    stuclasses_list = Stuclasse.objects.all()
    context = {
        'stuclasses2': stuclasses2,
        'stuclasses_list': stuclasses_list,
        'students': stud
    }
    return render(request, 'stuclasses.html', context)


def update_stuclasses(request, myid):
    stuc = Stuclasse.objects.get(id = myid)
    stuc.ClassID_id = request.POST['ClassID_id']
    stuc.Grade_id = request.POST['Grade_id']
    stuc.StudentID_id = request.POST['StudentID_id']
    stuc.save()
    messages.info(request, "Update success!!!")
    return redirect(stuclasses)
###################################################################################################################


