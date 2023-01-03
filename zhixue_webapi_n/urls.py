"""zhixue_webapi_n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. ARdd a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import path

urlpatterns = [
    path('info', get_info, name='info'),
    path('student/examList', stu_get_user_exam_list, name='get_user_exam_list'),
    path('student/recentExam', stu_get_recent_exam, name='get_recent_exam'),
    path('student/exams', stu_get_exams, name='get_exams'),
    path('student/examReport', stu_get_report_main, name='get_report_main'),
    path('student/checksheet', stu_get_checksheet, name='get_checksheet'),
    path('student/gradeClass', stu_get_zhixuebao_friendmanage, name='get_zhixuebao_friendmanage'),
    path('student/classStudents', stu_get_contact_students, name='get_contact_students'),
    path('student/teachers', stu_get_contact_teachers, name='get_contact_teachers'),
    path('student/examLevelTrend', stu_get_exam_level_trend, name='get_exam_level_trend'),
    path('student/subjectDiagnosis', stu_get_subject_diagnosis, name='get_subject_diagnosis'),

    path('teacher/markingSchoolClass', tch_get_marking_school_class, name='get_marking_school_class'),
    path('teacher/topic', tch_get_topic, name='get_topic'),
    path('teacher/examDetail', tch_get_scanrecognition, name='get_exam_detail'),
    path('teacher/subjectScore', tch_get_subject_score, name='get_subject_score'),
    path('teacher/simpleAnswerRecords', tch_get_simple_answer_records, name='get_simple_answer_records'),
]
