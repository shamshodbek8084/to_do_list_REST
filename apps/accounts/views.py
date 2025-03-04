from django.shortcuts import render
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
# Create your views here.   

class RegisterView(APIView):
    permission_classes = [AllowAny, ]
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status' : True,
                'msg' : "Registration is successfully"
            }
            return Response(data=data)
        data = {
            'status' : False,
            'msg' : "Smth is wrong",
            'errors' : serializer.errors
        }
        return Response(data=data)