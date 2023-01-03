from django.http import HttpResponse, HttpResponseBadRequest

from zhixue_webapi_n.zhixuewang import login as zxw_login
import json


def basic_error(error: Exception, code: int, err_msg: str) -> object:
    """
    抛出基本错误
    """
    ret = {
        'status': {
            'code': code,
            'message': err_msg,
            'error': str(error)
        },
    }
    return HttpResponseBadRequest(json.dumps(ret, indent=2, ensure_ascii=False), content_type='application/json')


def status_ok(result: object) -> object:
    ret = {
        'status': {
            'code': 0,
            'message': '成功'
        },
        'result': result
    }
    return HttpResponse(json.dumps(ret, indent=2, ensure_ascii=False), content_type='application/json')


def user_login(request):
    if request.GET.__contains__("usr") and request.GET.__contains__("pwd"):  # 旧版参数
        account = zxw_login(request.GET.get('usr'), request.GET.get('pwd'))
    else:
        account = zxw_login(request.GET.get('user'), request.GET.get('password'))
    return account


def get_info(request):
    try:
        return status_ok(user_login(request).info)
    except Exception as e:
        return basic_error(e, 1, '获取学生信息失败')


def stu_get_user_exam_list(request):
    try:
        return status_ok(
            user_login(request).get_user_exam_list(request.GET.get('pageIndex'), request.GET.get('pageSize')))
    except Exception as e:
        return basic_error(e, 2, '获取学生考试列表失败')


def stu_get_recent_exam(request):
    try:
        return status_ok(user_login(request).get_recent_exam)
    except Exception as e:
        return basic_error(e, 3, '获取学生最近考试列表失败')


def stu_get_exams(request):
    try:
        return status_ok(user_login(request).get_exams())
    except Exception as e:
        return basic_error(e, 4, '获取学生考试信息失败')


def stu_get_report_main(request):
    try:
        return status_ok(user_login(request).get_report_main(request.GET.get('examId')))
    except Exception as e:
        return basic_error(e, 5, '获取学生考试报告失败')


def stu_get_checksheet(request):
    try:
        return status_ok(user_login(request).get_checksheet(request.GET.get('subjectId'), request.GET.get('examId')))
    except Exception as e:
        return basic_error(e, 6, '获取学生考试试卷失败')


def stu_get_zhixuebao_friendmanage(request):
    try:
        return status_ok(user_login(request).get_zhixuebao_friendmanage())
    except Exception as e:
        return basic_error(e, 7, '获取当前年级所有班级失败')


def stu_get_contact_students(request):
    try:
        return status_ok(user_login(request).get_contact_students(request.GET.get('classId')))
    except Exception as e:
        return basic_error(e, 8, '获取班级学生信息失败')


def stu_get_contact_teachers(request):
    try:
        return status_ok(user_login(request).get_contact_teachers())
    except Exception as e:
        return basic_error(e, 9, '获取班级老师信息失败')


def stu_get_exam_level_trend(request):
    try:
        return status_ok(user_login(request).get_exam_level_trend(request.GET.get('examId'),
                                                                  request.GET.get('pageIndex'),
                                                                  request.GET.get('pageSize')))
    except Exception as e:
        return basic_error(e, 10, '获取学生考试等级趋势失败')


def stu_get_subject_diagnosis(request):
    try:
        return status_ok(user_login(request).get_subject_diagnosis(request.GET.get('examId')))
    except Exception as e:
        return basic_error(e, 11, '获取学生考试诊断失败')


def tch_get_marking_school_class(request):
    try:
        return status_ok(user_login(request).get_marking_school_class(request.GET.get('schoolId'),
                                                                      request.GET.get('subjectId')))
    except Exception as e:
        return basic_error(e, 13, '获取老师批改班级失败')


def tch_get_topic(request):
    try:
        return HttpResponse(user_login(request).get_topic(request.GET.get('userId'),
                                                          request.GET.get('paperId'),
                                                          result_type='return'))
    except Exception as e:
        return basic_error(e, 14, '获取原卷失败')


def tch_get_scanrecognition(request):
    try:
        return status_ok(user_login(request).get_scanrecognition(request.GET.get('examId')))
    except Exception as e:
        return basic_error(e, 15, '获取考试详情失败')


def tch_get_simple_answer_records(request):
    try:
        return status_ok(user_login(request).get_simple_answer_records(request.GET.get('classId'),
                                                                       request.GET.get('topicSetId'),
                                                                       request.GET.get('topicNumber'),
                                                                       request.GET.get('_type')))
    except Exception as e:
        return basic_error(e, 16, '获取考试答题记录失败')


def tch_get_subject_score(request):
    try:
        account = user_login(request)
        topic_set_id = request.GET.get('topicSetId')
        result = []
        for j in account.get_scanrecognition(request.GET.get('examId'))['result']['schoolList']:
            for each in account.get_marking_school_class(j['schoolId'], topic_set_id):
                for i in account.get_simple_answer_records(each['classId'], topic_set_id):
                    result.append(
                        {
                            'schoolId': i['schoolId'],
                            'schoolName': i['schoolName'],
                            'classId': i['classId'],
                            'className': each['className'],
                            'userId': i['userId'],
                            'userCode': i['userCode'],
                            'userName': i['userName'],
                            'score': i['score'],
                            'standardScore': i['standardScore']
                        }
                    )
        return status_ok(result)
    except Exception as e:
        return basic_error(e, 16, '获取考试成绩失败')
