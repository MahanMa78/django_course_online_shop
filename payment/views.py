import requests
import json

from django.shortcuts import render,get_object_or_404,redirect
from orders.models import Order
from config import settings
from django.http import HttpResponse
# Create your views here.


def payment_process(request):
    #get order id from session 
    order_id = request.session.get('order_id')

    #get the order object
    order = get_object_or_404(Order , id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price*10

    #hala bayad yek request be zarin-pal befrestim

    zarinpal_request_url = "https://api.zarinpal.com/pg/v4/payment/request.json"
    
    request_header = {
        "accept":"application/json",
        "content-type":"application/json",

    }

    request_data={
        'merchant_id':settings.ZARINPAL_MERCHENT_ID,
        'amount':rial_total_price,
        'description':f"#{order.id}:{order.user.first_name} {order.user.last_name}",
        'callback_url': 'https://127.0.0.1:8000',#'https://codingyar.com/payment/callback',bayad address site ro ke barmigarde ro bedim

    }


    res = requests.post(url=zarinpal_request_url,data=json.dumps(request_data),headers=request_header)

    data = res.json()["data"]
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0 :
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
    else:
        return HttpResponse("Error from zarinpal")