from django.urls import path
from .views import *

urlpatterns = [
    path('adminmanagepanelv1/<str:username>/<str:password>', admin_page),
    path('adminmanagepanelv1/<str:username>/<str:password>/addcoin', admin_addcoin_page),
    path('adminv1/user/delete', admin_delete_user),
    path('adminv1/coin/visible', admin_coin_visible),
    path('adminv1/coin/saveImg', admin_coin_img_save),
    path('adminv1/coin/add', admin_coin_add)
]
