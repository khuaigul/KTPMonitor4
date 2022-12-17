from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from .server import div
from .server import API_CF
from .server import people
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])


def main(request): 
    # request.GET['signin']
    return render(request, 'main/main.html')


def continue_registration(request):
    return render(request, 'main/continue_registration.html')


def div_info(request):
    return render(request, 'main/div_info.html')


def divisions(request):
    return render(request, 'main/divisions.html')


def menu(request):
    return render(request, 'main/menu.html')


def new_division(request):
    return render(request, 'main/new_division.html')


def registration(request):
    return render(request, 'main/registration.html')


def student_profile(request):
    return render(request, 'main/student_profile.html')


def students(request):
    return render(request, 'main/students.html')

@csrf_exempt 
def signin(request):
    if(request.method=='POST'):
        login = request.POST['login']
        password = request.POST['password']
        print(login, password)
# Вернуть True, если авторизация прошла успешно
    return JsonResponse({'status' : True})

@csrf_exempt 
def registrationRe(request):
    print('reg')
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        print(email, password);
    return JsonResponse({'status' : True})

@csrf_exempt
def profileData(request):
    if (request.method == 'POST'):
        date = request.POST["datebirth"]
    return JsonResponse({'status' : True})

@csrf_exempt
def studentData(request):
    if (request.method == 'POST'):
        qwe = dict()
        qwe={"students" : [ {"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "не выбрано"},{"nickname" : "qwer","surname" : "Петров", "name" : "Пётр", "secondname" : "Петрович", "div" : "A"},{"nickname" : "wertyui","surname" : "Смирнов", "name" : "Валерий", "secondname" : "Михайлович", "div" : "B"}, {"nickname" : "aaaanbvc","surname" : "Иванова", "name" : "Мария", "secondname" : "Ивановна", "div" : "A"},{"nickname" : "elele","surname" : "Крылова", "name" : "Анна", "secondname" : "Александровна", "div" : "не выбрано"}]}
     #   qwe = {"status" : True}
     #   print(request.POST["status"])
    return JsonResponse(qwe)

@csrf_exempt
def divisionsRe(request):
    if (request.method == 'POST'):
        ret = {"divisions" : ["A", "B", "C", "не выбрано"]}
    return JsonResponse(ret)

@csrf_exempt
def studentProfile(request):
    if (request.method == 'POST'):
        print(request.POST["nickname"])
        ret = {"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "A", "datebirth" : "12.05.2005", "school" : "Школа № 99", "form" : 10, "lastActivity" : "2 days ago"}
    return JsonResponse(ret)

@csrf_exempt
def сhangeDiv(request):
    if (request.method == 'POST'):
        print(request.POST["nickname"])
        print(request.POST["div"])
    return JsonResponse({"status" : True})

@csrf_exempt
def students_by_div(request):
    if (request.method == 'POST'):
        print(request.POST["div"])
        qwe={"students" : [ {"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "не выбрано"},{"nickname" : "qwer","surname" : "Петров", "name" : "Пётр", "secondname" : "Петрович", "div" : "A"},{"nickname" : "wertyui","surname" : "Смирнов", "name" : "Валерий", "secondname" : "Михайлович", "div" : "B"}, {"nickname" : "aaaanbvc","surname" : "Иванова", "name" : "Мария", "secondname" : "Ивановна", "div" : "A"},{"nickname" : "elele","surname" : "Крылова", "name" : "Анна", "secondname" : "Александровна", "div" : "не выбрано"}]}
    return JsonResponse(qwe)

@csrf_exempt
def newDivisionRe(request):
    if (request.method == "POST"):
        print(request.POST["name"])
    return JsonResponse({"status" : True})