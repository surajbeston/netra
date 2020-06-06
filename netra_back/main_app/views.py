from django.shortcuts import render
import string
import random
from django.http import JsonResponse
from main_app.models import Fleet

all_chars = string.ascii_letters + string.digits
def home(request):

    rand_id = ''.join([all_chars[random.randrange(62)] for _ in range(20)])
    return render(request, "main_app/home.html",{"id": rand_id})

def id_json(request):
    rand_id = ''.join([all_chars[random.randrange(62)] for _ in range(20)])
    return JsonResponse({"_id": rand_id})

def fleet(request, num):
    ids = []
    for _ in range(int(num)):
        rand_id = ''.join([all_chars[random.randrange(62)] for _ in range(20)])
        ids.append(rand_id)
    fleet_id = "fleet_" + ''.join([all_chars[random.randrange(62)] for _ in range(20)]) 
    obj = Fleet(fleet_id = fleet_id, ids = ','.join(ids))
    obj.save()
    print (','.join(ids))
    return JsonResponse({"fleet_id": fleet_id ,"ids": ids })
