from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import admin_required
from .models import Korisnici, Predmeti, Upisi
from .forms import KorisniciForm, PredmetiForm, AssignSubjectForm, UpisiForm

def home(request):
    data = "Hello!"
    return render(request, 'home.html', {"data": data})

def get_all_students(request):
    students = Korisnici.objects.filter(role='stu')
    return render(request, 'students.html', {'students': students})

def add_student(request):
    if request.method == 'GET':
        form = KorisniciForm()
        return render(request, 'add_student.html', {"form": form})
    elif request.method == 'POST':
        form = KorisniciForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')

def edit_student(request, id):
    student = Korisnici.objects.get(pk=id)
    if request.method == 'GET':
        form = KorisniciForm(instance=student)
        return render(request, 'edit_student.html', {"form": form})
    elif request.method == 'POST':
        form = KorisniciForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            return HttpResponseNotAllowed()

        
def get_all_professors(request):
    professors = Korisnici.objects.filter(role='prof')
    return render(request, 'professors.html', {'professors': professors})

def add_professor(request):
    if request.method == 'GET':
        form = KorisniciForm()
        return render(request, 'add_professor.html', {"form": form})
    elif request.method == 'POST':
        form = KorisniciForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professors')
        
def edit_professor(request, id):
    professor = Korisnici.objects.get(pk=id)
    if request.method == 'GET':
        form = KorisniciForm(instance=professor)
        return render(request, 'edit_professor.html', {"form": form})
    elif request.method == 'POST':
        form = KorisniciForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professors')
        else:
            return HttpResponseNotAllowed()
        
def get_subject_list(request):
    subjects = Predmeti.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'GET':
        form = PredmetiForm()
        return render(request, 'add_subject.html', {"form": form})
    elif request.method == 'POST':
        form = PredmetiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        
def edit_subject(request, id):
    subject = Predmeti.objects.get(pk=id)
    if request.method == 'GET':
        form = PredmetiForm(instance=subject)
        return render(request, 'edit_subject.html', {"form": form})
    elif request.method == 'POST':
        form = PredmetiForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        else:
            return HttpResponseNotAllowed()

@admin_required
def assign_subject_to_professor(request, professor_id):
    subject = Predmeti.objects.get(pk=professor_id)
    if request.method == 'POST':
        form = AssignSubjectForm(request.POST)
        if form.is_valid():
            professor = form.cleaned_data['professor']
            subject = form.cleaned_data['subject']
            subject.nositelj = professor
            subject.save()
            return redirect('subject_list')
    else:
        form = AssignSubjectForm()
    return render(request, 'assign_subject_professor.html', {'form': form})

def upisni_list(request, student_id):
    student = get_object_or_404(Korisnici, id=student_id)
    enrolled_subjects = Upisi.objects.filter(student_id=student_id)
    subjects = Predmeti.objects.all()
    return render(request, 'upisni_list.html', {'student': student, 'subjects': subjects, 'enrolled_subjects': enrolled_subjects})

def enroll_subject(request, student_id):
    student = get_object_or_404(Korisnici, id=student_id)
    subjects = Predmeti.objects.all()
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')  
        subject = get_object_or_404(Predmeti, id=subject_id)
        created = Upisi.objects.get_or_create(student_id=student, predmet_id=subject)
        if created:
            created[0].status = 'upis'
            created[0].save()
        else:
            pass
    enrolled_subjects = Upisi.objects.filter(student_id=student)
    return render(request, 'upisni_list.html', {'student': student, 'subjects': subjects, 'enrolled_subjects': enrolled_subjects})


def unenroll_subject(request, student_id):
    student = get_object_or_404(Korisnici, id=student_id)

    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(Predmeti, id=subject_id)

        enrollment = Upisi.objects.get(student_id=student, predmet_id=subject)
        enrollment.delete()

    subjects = Predmeti.objects.all()
    enrolled_subjects = Upisi.objects.filter(student_id=student)

    return render(request, 'upisni_list.html', {'student': student, 'subjects': subjects, 'enrolled_subjects': enrolled_subjects})

@login_required
def professor_subjects(request):
    subjects = Predmeti.objects.filter(nositelj=request.user)
    return render(request, 'professor_subjects.html', {'subjects': subjects})

@login_required(login_url='login')
def enrolled_students_list(request, subject_id):
    subject = Predmeti.objects.get(pk=subject_id)
    enrollments = Upisi.objects.filter(predmet_id=subject)
    enrolled_students = [enrollment.student_id_id for enrollment in enrollments]
    students = Korisnici.objects.filter(id__in=enrolled_students)
    return render(request, 'enrolled_students_list.html', {'subject': subject, 'enrolled_students': students})

def edit_subject_status(request, student_id, subject_id):
    enrollment = get_object_or_404(Upisi, student_id=student_id, predmet_id=subject_id)

    if request.method == 'POST':
        form = UpisiForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = UpisiForm(instance=enrollment)

    return render(request, 'edit_subject_status.html', {'form': form})

def subject_status_list(request, status):
    students = Korisnici.objects.filter(upisi__status=status)
    return render(request, 'subject_status_list.html', {'students': students, 'status': status})

@admin_required
def view_student_status(request):
    students = Korisnici.objects.filter(status='red')
    student_count = students.count()
    return render(request, 'view_student_status.html', {'students': students, 'student_count': student_count})

@admin_required
def view_student_status_ne(request):
    students = Korisnici.objects.filter(status='izv')
    student_count = students.count()
    return render(request, 'view_student_status_ne.html', {'students':students, 'student_count': student_count})