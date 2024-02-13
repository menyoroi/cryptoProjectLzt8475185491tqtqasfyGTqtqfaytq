import json

from django.http import HttpRequest, JsonResponse, HttpResponseNotFound
from main.models import User, Asset, UserAdmin
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import secrets


def admin_page(request: HttpRequest, username, password):
    list_user = User.objects.all()
    list_asset = Asset.objects.all()
    admin = UserAdmin.objects.filter(username=username, password=password)
    if len(admin) == 1:
        return render(request, 'admin.html', context={'users': list_user, 'assets': list_asset})
    else:
        return HttpResponseNotFound()

def admin_addcoin_page(request: HttpRequest, username, password):
    admin = UserAdmin.objects.filter(username=username, password=password)
    if len(admin) == 1:
        return render(request, 'addCoin.html')
    else:
        return HttpResponseNotFound()

@csrf_exempt
def admin_delete_user(request: HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'user_id' in body and 'username' in body and 'password' in body:
            username = body['username']
            password = body['password']
            user_id = body['user_id']
            admin = UserAdmin.objects.filter(username=username, password=password)
            if len(admin) == 1:
                user = User.objects.filter(id=user_id)
                if len(user) == 1:
                    user[0].delete()
                    return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'Error'})


@csrf_exempt
def admin_coin_visible(request: HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'asset_id' in body and 'username' in body and 'password' in body and 'asset_status' in body:
            username = body['username']
            password = body['password']
            asset_id = body['asset_id']
            asset_status = body['asset_status']
            admin = UserAdmin.objects.filter(username=username, password=password)
            if len(admin) == 1:
                asset = Asset.objects.filter(id=int(asset_id))
                if len(asset) == 1:
                    asset[0].visible = bool(asset_status)
                    asset[0].save()
                    return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'Error'})


@csrf_exempt
def admin_coin_img_save(request: HttpRequest):
    if request.method == 'POST':
        headers = request.headers
        if 'username' in headers and 'password' in headers:
            username = headers['username']
            password = headers['password']
            admin = UserAdmin.objects.filter(username=username, password=password)
            if len(admin) == 1:
                try:
                    uploaded_file = request.FILES['file']
                    new_file_name = f'{secrets.token_hex(50)}_{uploaded_file.name}'
                    with open(f'main/static/img/ico coin/{new_file_name}', 'wb') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                    return JsonResponse({'status': True, 'filename': new_file_name})
                except:
                    pass
        return JsonResponse({'status': False})


@csrf_exempt
def admin_coin_add(request: HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'coin_name' in body and 'coin_shrt_name' in body and 'username' in body and 'password' in body and 'img_name' in body:
            username = body['username']
            password = body['password']
            coin_name = body['coin_name']
            coin_shrt_name = body['coin_shrt_name']
            img_name = body['img_name']
            admin = UserAdmin.objects.filter(username=username, password=password)
            if len(admin) == 1:
                Asset(name=coin_name, short_name=coin_shrt_name, img=img_name).save()
                return JsonResponse({'status': True})
        return JsonResponse({'status': False})
