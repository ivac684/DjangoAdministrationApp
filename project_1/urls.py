"""
URL configuration for project_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_1 import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('students/', views.get_all_students, name="students"),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('professors/', views.get_all_professors, name="professors"),
    path('add_professor/', views.add_professor, name='add_professor'),
    path('edit_professor/<int:id>', views.edit_professor, name='edit_professor'),
    path('subject_list/', views.get_subject_list, name='subject_list'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_subject/<int:id>', views.edit_subject, name='edit_subject'),
    path('assign_subject_professor/<int:professor_id>', views.assign_subject_to_professor, name='assign_subject_professor'),
    path('upisni_list/<int:student_id>/', views.upisni_list, name='upisni_list'),
    path('enroll_subject/<int:student_id>/', views.enroll_subject, name='enroll_subject'),
    path('unenroll_subject/<int:student_id>/', views.unenroll_subject, name='unenroll_subject'),
    path('enrolled_students_list/<int:subject_id>/', views.enrolled_students_list, name='enrolled_students_list'),
    path('professor_subjects/', views.professor_subjects, name='professor_subjects'),
    path('enrolled_students_list/<int:subject_id>/', views.enrolled_students_list, name='enrolled_students_list'),
    path('edit_subject_status/<int:student_id>/<int:subject_id>/', views.edit_subject_status, name='edit_subject_status'),
    path('subject_status_list/<str:status>/', views.subject_status_list, name='subject_status_list'),
    path('view_student_status/', views.view_student_status, name='view_student_status'),
    path('view_student_status_ne/', views.view_student_status_ne, name='view_student_status_ne'),
]
