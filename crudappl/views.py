from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
from crudappl.models import users
from crudappl.serializers import userSerializer
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        customers = users.objects.all()
        customers_serializer = userSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
    
        customer_data = JSONParser().parse(request)
        customer_serializer = userSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt 
def user_detail(request, pk):
    try: 
        customer = users.objects.get(pk=pk) 
    except users.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customer_serializer = userSerializer(customer) 
        return JsonResponse(customer_serializer.data) 
 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = userSerializer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customer.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)