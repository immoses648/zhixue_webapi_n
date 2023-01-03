# 智学网 WebAPI 新版

### 📄快速开始

输入如下命令快速搭建API服务。

```bash
git clone https://github.com/immoses648/zhixue_webapi_n
cd zhixue_webapi_n
pip install -r requirements.txt
python manage.py runserver
```

### api接口url
```
    path('info', get_info, name='获取登录用户信息'), 
    
    path('student/examList', stu_get_user_exam_list, name='获取学生考试列表'),
    path('student/recentExam', stu_get_recent_exam, name='获取学生最新的考试'),
    path('student/exams', stu_get_exams, name='获取学生全部考试'),
    path('student/examReport', stu_get_report_main, name='获取学生单场考试报告'),
    path('student/checksheet', stu_get_checksheet, name='获取学生原卷'),
    path('student/gradeClass', stu_get_zhixuebao_friendmanage, name='获取年级内班级'),
    path('student/classStudents', stu_get_contact_students, name='获取指定班级学生'),
    path('student/teachers', stu_get_contact_teachers, name='获取教师'),
    path('student/examLevelTrend', stu_get_exam_level_trend, name='获取学生等级趋势'),
    path('student/subjectDiagnosis', stu_get_subject_diagnosis, name='获取学生学科诊断'),

    path('teacher/markingSchoolClass', tch_get_marking_school_class, name='获取参与考试的班级'),
    path('teacher/topic', tch_get_topic, name='教师获取学生原卷'),
    path('teacher/examDetail', tch_get_scanrecognition, name='获取考试详情'),
    path('teacher/subjectScore', tch_get_subject_score, name='获取某考试中所有人某科的分数'),
    path('teacher/simpleAnswerRecords', tch_get_simple_answer_records, name='获取某班某科（某题）的分数'),
```
