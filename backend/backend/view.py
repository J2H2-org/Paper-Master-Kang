from django.shortcuts import render, redirect
import requests
from django.views import View
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse

def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'index.html', _context)

def kakaoLoginLogic(request):
    _restApiKey = 'b4f6f8f6c4b053afea4c10388afad5f0'
    _redirectUrl = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = 'b4f6f8f6c4b053afea4c10388afad5f0'
    _redirect_uri = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'loginSuccess.html')
