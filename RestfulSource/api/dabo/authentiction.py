from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .. import models
from rest_framework import exceptions
from django.http import JsonResponse

class CustomAuthentication(SessionAuthentication):
    """
    基于token的自定义认证
    """

    def authenticate(self, request):
        tk = request.query_params.get('tk')
        token_obj = models.Token.objects.filter(token=tk).first()
        if token_obj:
            return (token_obj.user, token_obj)
        raise exceptions.AuthenticationFailed('认证失败')

    def authenticate_header(self, request):
        pass



class AAAuthentication(object):
    """
    这个类，如果有多个视图需要认证，就多继承这个类，优先继承这个类，才存在的，如果写到settings里，那就是全局的引用，所有的视图都要校验
    根据情况不同，可以自行更改
    """
    authentication_classes = [CustomAuthentication]

    def gen_token(self, user):
        """
        这个函数写这类里面纯属闲的蛋疼，都是类，搞个函数，影响心情，就加这个类里了，如果有后续视图需要hash，也可以用
        :param user: 传递用户名，别处用，也无所谓
        :return: 用户名+当前时间的hash值
        """
        import hashlib
        import time
        hash = hashlib.md5(user.encode('utf-8'))
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()
