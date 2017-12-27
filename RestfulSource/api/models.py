from django.db import models

class UserGroup(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    user_type_choices = (
        (1, '普通用户'),
        (2, 'vip用户'),
        (3, '超级用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)
    ug = models.ForeignKey(UserGroup, default=1, on_delete=None)

class Token(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=None)
    token = models.CharField(max_length=64)


