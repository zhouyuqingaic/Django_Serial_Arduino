from django.shortcuts import render
from django.http import HttpResponse
import json
import time
import serial

# Create your views here.
def index(request):
    return render(request,'car_control/index.html')

def car_action(request,car_forward):
     
    
    print(str(time.time())+'------action:'+car_forward)
    
    se=serial.Serial('/dev/ttyUSB0',9600)
    se.write(car_forward.strip().encode())

    print('-----From Serial-----{}:{}'.format(
        car_forward,se.readline().decode().strip()
    ))
    return HttpResponse(str(time.time())+'------action:'+car_forward)
     
    