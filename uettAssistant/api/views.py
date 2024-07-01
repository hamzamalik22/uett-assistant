from rest_framework.decorators import api_view
from uettApp.models import *
from titlepage.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def getRoutes(request, format=None):
    routes = [
        {"GET": "/api/departments"},
        {"GET": "/api/departments/id"},
        {"GET": "/api/subjects"},
        {"GET": "/api/subjects/id"},
        {"GET": "/api/semesters"},
        {"GET": "/api/semesters/id"},
        {"POST": "/api/titlepage"},
    ]
    return Response({"Routes": routes})


@api_view(["GET"])
def getDepartments(request, format=None):
    deps = Department.objects.all()
    serializer = DepartmentSerializers(deps, many=True)
    return Response({"Departments": serializer.data})


@api_view(["GET"])
def getDepartment(request, pk, format=None):
    dep = Department.objects.get(id=pk)
    serializer = DepartmentSerializers(dep, many=False)
    return Response({"Department": serializer.data})


@api_view(["GET"])
def getSubjects(request, format=None):
    subs = Subject.objects.all()
    serializer = SubjectSerializers(subs, many=True)
    return Response({"Subjects": serializer.data})


@api_view(["GET"])
def getSubject(request, pk, format=None):
    sub = Subject.objects.get(id=pk)
    serializer = SubjectSerializers(sub, many=False)
    return Response({"Subject": serializer.data})


@api_view(["GET"])
def getSemesters(request, format=None):
    sems = Semester.objects.all()
    serializer = SemesterSerializers(sems, many=True)
    return Response({"Semesters": serializer.data})


@api_view(["GET"])
def getSemester(request, pk, format=None):
    sem = Semester.objects.get(id=pk)
    serializer = SemesterSerializers(sem, many=False)
    return Response({"Semester": serializer.data})


@api_view(["POST"])
def setTitlePage(request, format=None):
    titlePage = TitlePage.objects.all()
    serializer = TitlePageSerializers(titlePage, many=True)
    return Response({"TitlePage": serializer.data})


# @api_view(['GET','PUT','DELETE'])
# def getTask(request,id, format=None):
#     try:
#         task = Task.objects.get(pk=id)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProjectSerializers(task)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProjectSerializers(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
