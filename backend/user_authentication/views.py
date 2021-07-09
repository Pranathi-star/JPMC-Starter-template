from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import Group
from twilio.rest import Client
from .serializers import UserSerializer
from .models import custom_user
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import hashlib

@api_view(['GET','POST'])
def login(request):
    if(request.method=="POST"):
        user = request.data
        username = user['username']
        password = user['password']
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        CustomUser = custom_user.objects.filter(username=username)
        if(CustomUser.count()==0):
            return JsonResponse({"message":"User doesn't exist."})
        if(hashed_pass==CustomUser[0].password):
            return JsonResponse({'message':'Logged in successfully!'})
        return JsonResponse({"message":"Password doesn't match. Try again!", "username":username})


@csrf_exempt
@api_view(['GET','POST'])
def register_user(request):
    if(request.method=="POST"):
        serializer = UserSerializer(data=request.data)
        hashed_pass = hashlib.md5(request.data['password'].encode())
        serializer.is_valid(raise_exception=True)
        serializer.save(group='S', password = hashed_pass.hexdigest())
        return JsonResponse({"message":"Registration successful!"})

