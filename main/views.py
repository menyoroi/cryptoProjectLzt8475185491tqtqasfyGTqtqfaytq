from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.cache import cache
from .models import Asset, User, UserToken
from django.views.decorators.csrf import csrf_exempt
import json
import secrets


def index_page(request: HttpRequest):
    assets = Asset.objects.all().values()
    tickers = cache.get('tickers')
    security_key = None
    user = None
    if 'auth_token' in request.session:
        auth_token = request.session.get('auth_token')
        user_token = UserToken.objects.filter(token=auth_token)
        if len(user_token) == 1:
            user = User.objects.filter(email=user_token[0].email)
            if len(user) != 1:
                user = None
            else:
                user = user[0]
    if 'securityKey' in request.session:
        security_key = request.session.get('securityKey')
    for asset in assets:
        short_name = asset['short_name']
        if tickers:
            if short_name in tickers:
                asset['price'] = tickers[short_name]['last']
                asset['change'] = tickers[short_name]['percentage']
                asset['change_status'] = 'up'
                if '-' in str(asset['change']):
                    asset['change_status'] = 'down'
                    asset['change'] = abs(float(tickers[short_name]['percentage']))
        if 'price' not in asset:
            asset['price'] = 0
            asset['change'] = 0
            asset['change_status'] = 'up'
    return render(request, 'index.html', context={'assets': assets, 'securityKey': security_key, 'user': user})



@csrf_exempt
def request_auth(request: HttpRequest, type='login'):
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'email' and 'password' and 'securityKey' in body:
            email = body['email']
            password = body['password']
            security_key = body['securityKey']
            if 'securityKey' in request.session:
                if str(security_key) == str(request.session.get('securityKey')):
                    user = User.objects.filter(email=email)
                    if type == 'login':
                        if len(user) != 1 or user[0].email != str(email) or user[0].password != str(password):
                            return JsonResponse({'error': 'Email or password invalid.'})
                    elif type == 'reg':
                        if len(user) != 1:
                            new_user = User(email=email, password=password)
                            new_user.save()
                        else:
                            return JsonResponse({'error': 'The email has already been registered.'})
                    new_token = UserToken(email=email, token=secrets.token_hex(50))
                    new_token.save()
                    request.session['auth_token'] = new_token.token
                    return JsonResponse({'auth': True})
        return JsonResponse({'error': 'Something went wrong.'})




