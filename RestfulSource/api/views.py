
# ------------------- 渲染   -------------------
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from . import models
from rest_framework.renderers import JSONRenderer,HTMLFormRenderer,AdminRenderer,BrowsableAPIRenderer

class MySerializer(serializers.ModelSerializer):
    # zhangkai = serializers.CharField(source='ug.title')  # 自定义字段
    class Meta:
        model = models.UserInfo
        fields = "__all__"

class UserIndex(APIView):
    """
    根据用户请求url的后缀的不同，显示不同的页面
        http://127.0.0.1:8881/v2/users/  # 最常用的：BrowsableAPIRenderer
        http://127.0.0.1:8881/v2/users.form  # 不常用：HTMLFormRenderer
        http://127.0.0.1:8881/v2/users.admin  # 不常用
        http://127.0.0.1:8881/v2/users.json  # 最常用的：JSONRenderer
    """
    # 最常用的两个渲染模板，和局部应用
    # renderer_classes = [JSONRenderer，BrowsableAPIRenderer]

    def get(self, request, *args, **kwargs):

        user_list = models.UserInfo.objects.all().first()
        src = MySerializer(instance=user_list, many=False)
        return Response(src.data)


