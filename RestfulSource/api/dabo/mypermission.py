from rest_framework.permissions import BasePermission
from .. import views


class MyPermission(BasePermission):
    message = '无权限访问qqqqq'
    def has_permission(self, request, view):


        if isinstance(view, views.GroupViews) and request._request.method == 'GET':
            return False
        return True


    def has_object_permission(self, request, view, obj):
        """
        from rest_framework.generics import GenericAPIView

        这个方法之有在试图函数不继承APIView,而继承GenericAPIView，进行权限验证是有用到
        其他的地方没有用到,所以，暂时略过不表
        class UserView(GenericAPIView):
            def get(self, request, *args, **kwargs):
                pass
        """
        pass