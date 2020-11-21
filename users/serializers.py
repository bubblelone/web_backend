from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        re_data = {}
        try:
            data = super().validate(attrs)
        except:
            re_data['message'] = '用户名或密码错误'
            re_data['code'] = "400"

            return re_data
        re_data['data'] = data
        re_data['code'] = "200"
        re_data['message'] = '登录成功'
        re_data['username'] = self.user.username
        re_data['id'] = self.user.id


        return re_data