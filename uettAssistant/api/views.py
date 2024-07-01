from rest_framework.decorators import api_view
from uettApp.models import *
from titlepage.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getRoutes(request, format=None):
        routes = [
            {'GET' : '/api/departments'},
            {'GET' : '/api/departments/id'},
            {'GET' : '/api/subjects'},
            {'GET' : '/api/subjects/id'},
            {'GET' : '/api/semesters'},
            {'GET' : '/api/semesters/id'},
            {'GET' : '/api/titlepage'},
        ]
        return Response({'Routes': routes})
    

@api_view(['GET'])
def getDepartment(request, format=None):
        deps = Department.objects.all()
        serializer = DepartmentSerializers(deps, many=True)
        return Response({'Departments':serializer.data})
    
        
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
