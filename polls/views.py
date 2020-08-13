from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,HttpResponse
from rest_framework import status
# from polls.serializers import MemberDetailsSerializer, DateSerializer, MemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from polls.models import Member_Details, Member, Date
import json
from django.http import JsonResponse
from django.core.serializers import serialize

def members_detail(request):  
    list_contact=[]
   # data = Date.objects.get("user_id")
    #print("-------------",data)
    #number_data = Member.objects.filter(members=1).values("members__real_name","members__tz","ok")
    number_data = Member_Details.objects.filter(activity_periods=1).values("activity_periods__user_id","tz","real_name","activity_periods__start_time","activity_periods__end_time")
    print(type(number_data))
    # print(number_data["members__activity_periods__start_time"])
    print(number_data.values())
    for i in number_data:
            list_contact.append({
            # 'ok' : i["ok"],
            'id':i["activity_periods__user_id"], 
            'real_name' : i["real_name"],
            'tz' : i["tz"],
            "activity_periods": [  {
            'start_time' : i["activity_periods__start_time"],
            'end_time' : i["activity_periods__end_time"]}
            ]
    })
    print(list_contact)
    final_list = [{
                "ok": "true",
	            "members":list_contact
                }]

    return JsonResponse(final_list, safe=False)
    #return JsonResponse(list_contact, safe=False) 
    
    #a = serialize('json', number_data)
    #return HttpResponse(json.dumps(list_contact))
    #return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    # return JsonResponse({Json})
     #   print(i["members__real_name"])
      #  print(i["members__tz"])
       # print(i["ok"])
    # for x in number_data:
    #    list_contact.append({
    #       'activity_periods' : x.activity_periods,
    #       'ok' : x.ok,
    #        'real_name' : x.real_name,
    #       'tz' : x.tz
    #    })

    # return JsonResponse({"message":"success",
    # "id":data.id,
    # # "real_name":data.real_name,
    # # "tz":data.tz,
    # # "activity_periods": data.activity_periods,
    # },safe=False)
    