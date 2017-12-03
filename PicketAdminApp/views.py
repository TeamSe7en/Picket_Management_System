from django.shortcuts import render
from django.utils import timezone
from .models import Picket, Task, Person
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Picket.objects.all().order_by('date')
    print(posts)
    return render(request, 'PicketAdminApp/post_list.html',{'posts': posts})

def check_task(request):
    task = Task.objects.filter(status=True).first()
    task_json = json.dumps({'id':task.id,
                            'task':task.name,
                            'task_data':task.data})
    return HttpResponse(task_json, content_type='application/json')

def all_person(request):
    data_person = Person.objects.all()
    data = [person.telegram_id for person in data_person]

    data_json = json.dumps({'id_person':data})
    return HttpResponse(data_json, content_type='application/json')

@csrf_exempt
def add_person(request):
    #data = request.POST.get()
    #name = request.POST.get('name')
    info_to_add = json.loads(request.body)
    new_person = Person(telegram_id=info_to_add['person_id'], name=info_to_add['name'],
                        surname=info_to_add['surname'], patronymic=info_to_add['patronymic'],
                        station=info_to_add['metro'])
    new_person.save()
    print(info_to_add)
    #old_person = Person.objects.get(telegram_id=123121)
    #old_person.delete()
    #person = Person(telegram_id=123121, name=name, surname='gustav', patronymic='lol', station='baumanskaya')
    #person.save()
    return HttpResponse(status=200)

def set_person_for_picket(request):
    info_to_set = json.loads(request.body)
    try:
        picket = Picket.objects.get(info_to_set['picket_date'])
        picket.persons = info_to_set['agree_persons']
        picket.save()
        return HttpResponse(status=200)
    except Picket.DoesNotExist:
        print('нет пикета с этой датой')
        return HttpResponse(status=500)
    except Picket. MultipleObjectsReturned:
        print('существует несколько пикетов с этой датой')
        return HttpResponse(status=500)


def task_complete(request):
    info_to_completion = json.loads(request.body)
    id_task = info_to_completion['id']
    try:
        task = Task.objects.get(id = id_task)
        task.update(status = False)
        return HttpResponse(status=200)
    except Task.DoesNotExist:
        print('нет задачи с этой датой')
        return HttpResponse(status=500)
    except Task.MultipleObjectsReturned:
        print('существует несколько задач с этим id')
        return HttpResponse(status=500)

