# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# ----------------- 版本控制 ---------------

# from rest_framework.versioning import URLPathVersioning

class UserIndex(APIView):
    # versioning_class = URLPathVersioning  # 当前类内应用

    def get(self, request, *args, **kwargs):
        # 反向生成url
        print(request.versioning_scheme.reverse(viewname='xx', request=request))  # http://127.0.0.1:8881/v2/users/
        print(request.version)  # 获取版本
        self.dispatch

        return Response(8888)

class GroupViews(APIView):

    def get(self, request):

        return Response('group')
