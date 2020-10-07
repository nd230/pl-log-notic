import json
import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.db import transaction, DatabaseError
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pltplconf.models import Pljob, PlTaskSetting

@require_http_methods(["GET"])
def index(request):
    """输出首页，index.html"""
    return render(request, 'pltplconf/index.html')

@require_http_methods(["GET"])
def task_list(request):
    """返回任务列表"""
    tasks = PlTaskSetting.objects.order_by('-id').all()
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = []
    results = []
    for task in list:
        results.append({"id": task.id, "name": task.task_name})
    return response(data={
        "list": results
    })

@require_http_methods(["POST"])
@csrf_exempt
def task_add(request):
    """新建任务，不包含详细的配置，只有名称"""
    datas = json.loads(request.body.decode())
    params = datas["params"]

    # 任务名称不能为空
    if re.compile(r"^\s*$").match(params["taskName"]) is not None:
        return response(-1, message="任务名不能为空。")

    # 如果数据库中已经有名称相同的任务，那么不能重复创建
    if PlTaskSetting.objects.filter(task_name=params["taskName"]).count() > 0:
        return response(-2, message="任务名已存在，无法重复创建。")

    taskSetting = PlTaskSetting(task_name=params["taskName"])
    job = Pljob(
        last_exec_time = timezone.now(),
        next_exec_time = timezone.now(),
        delay_sec = 1,
        job_name = taskSetting.task_name,
        task_setting = taskSetting,
        system_type = 5 # 5 专门表示关联 PlTaskSetting 的
    )

    success = True
    try:
        with transaction.atomic():
            taskSetting.save()
            job.save()
    except DatabaseError:
        success = False

    if success:
        return response(0, data={"id": taskSetting.id})
    else:
        return response(1)

def response(code=0, data={}, message=""):
    """统一返回格式"""
    codes = { # 公共的返回消息，code >= 0，如果业务需要返回定制消息的，code取负数
        0: "success",
        1: "数据库写入失败"
    }
    if code in codes:
        return JsonResponse({"code": code, "message": codes[code], "data": data})
    else:
        return JsonResponse({"code": code, "message": message, "data": data})