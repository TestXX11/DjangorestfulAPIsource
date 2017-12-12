# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

class UserIndex(APIView):

    def get(self, *args, **kwargs):
        return Response(8888)