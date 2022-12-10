from django.shortcuts import render
from .serializers import CourseSerializer
from django.http import JsonResponse, HttpResponse
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def course_api(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def course_details(request, pk):
    try:
        course = Course.objects.get(pk=pk)

    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False, status=400)

    elif request.method == "DELETE":
        course.delete()
        return HttpResponse(status=204)

        
