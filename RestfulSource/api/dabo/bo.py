

from rest_framework.authentication import SessionAuthentication
from .. import models
from rest_framework import exceptions


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




# 以下为全局认证的代码

# class CustomAuthentication(SessionAuthentication):
#     """
#     自定义认证，必须集成源码的相对应的类，和方法
#     """
#
#     def authenticate(self, request):
#         # from rest_framework import exceptions
#         return ('bbbbbbbbbbbb','123')
#         # raise exceptions.AuthenticationFailed('自定义认证信息')
#
#
#     def authenticate_header(self, request):
#         pass
