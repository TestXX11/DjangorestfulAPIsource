from rest_framework.throttling import SimpleRateThrottle


class MyUserRateThrottle(SimpleRateThrottle):
    """
    自定义登陆用户的throttle，
    下面两个方法都必须实现
    """

    scope = 'login_user'  # 跟settings一致就行，这个无所谓

    def allow_request(self, request, view):
        # if request is anonymous,return true
        # print(request.user)
        if not request.user:
            return True
        # 获取当前访问用户的用户名
        # print(request.user.user)
        self.key = request.user.user
        self.history = self.cache.get(self.key, [])
        self.now = self.timer()
        while self.history and self.history[-1] <= self.now - self.duration:
            # 就把那一条记录pop掉
            self.history.pop()
        # 如果历史记录>= 自定义的频率次数，如5
        if len(self.history) >= self.num_requests:
            # 返回false
            return self.throttle_failure()
        # 上面几步没问题，请求通过
        return self.throttle_success()

    def get_cache_key(self, request, view):
        # print(self.scope)

        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request),
        }


class MyAnonymousRateThrottle(SimpleRateThrottle):
    """
    只处理匿名用户的throttle，
    下面两个方法都必须实现
    """
    scope = 'anonymous_user'

    def allow_request(self, request, view):
        # 如果是登陆用户，这个类就不做处理
        if request.user:
            return True

        self.key = self.get_cache_key(request, view)

        # 这一步我们不自定义的话，默认不限制
        if self.key is None:
            return True
        self.history = self.cache.get(self.key, [])
        # 当前时间
        self.now = self.timer()

        # Drop any requests from the history which have now passed the
        # throttle duration
        # 如果历史记录中的最远的那一条记录，  当前时间-自定义的访问频率时间m=60duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[period[0]]
        while self.history and self.history[-1] <= self.now - self.duration:
            # 就把那一条记录pop掉
            self.history.pop()
        # 如果历史记录>= 自定义的频率次数，如5
        if len(self.history) >= self.num_requests:
            # 返回false
            return self.throttle_failure()
        # 上面几步没问题，请求通过
        return self.throttle_success()

    def get_cache_key(self, request, view):
        # print(self.scope)

        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request),
        }