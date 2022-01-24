from django.shortcuts import redirect
import requests
#from backend.settings import SOCIAL_OUTH_CONFIG
from django.views import View
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

def kakaoLoginLogic(request):
    _restApiKey = 'b4f6f8f6c4b053afea4c10388afad5f0'
    _redirectUrl = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginView(request):
    _qs = request.GET.get('code')
    _restApiKey = 'b4f6f8f6c4b053afea4c10388afad5f0'
    _redirect_uri = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
    url = 'https://kauth.kakao.com/oauth/token'
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    body = {'grant_type': 'authorization_code',
            'client_id' : 'b4f6f8f6c4b053afea4c10388afad5f0',
            'redirect_uri': 'http://127.0.0.1:8000/accounts/kakao/login/callback/',
            'code' : _qs
            }
    _res = requests.post(url,headers=headers, data = body)
    _access_token = _res.json()
     access_token = json.loads(_res.text).get('access_token')
     request.session['access_token'] = _access_token['access_token']
     request.session.modified = True
    _user_url = 'https://kapi.kakao.com/v2/user/me'
    auth = "Bearer "+ _access_token['access_token']
    HEADER = {
        'Authorization' : auth
        'Contest-type' : 'applicaton/x-www-form-urlencoded;charset=utf-8'
    }
    _user_result = requests.get(_user_url, headers=HEADER)
    _user_result = json.loads(_user_result.text)
    return Response(_user_result.text)






