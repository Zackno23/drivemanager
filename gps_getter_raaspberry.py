from pyicloud import PyiCloudService
from two_way_auth import get_gps_from_iphone
import sqlite3
from cal_rho import get_distance
import time
from datetime import datetime
from firebase import firebase
api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

# 緯度経度をリストで保存

'''
pythonでfirebase
参考URL：https://www.youtube.com/watch?v=rKuGCQda_Qo
'''
prev_gps = ()
distnace = 0

firebase = firebase.FirebaseApplication('https://drive-manager-18863.firebaseio.com/', None)

for i in range(5):

    gps = get_gps_from_iphone(api)
    if prev_gps != ():
        distnace += get_distance(prev_gps, gps)

    data = {
        '目的地': '市役所',
        '仕事内容': 'MTG',
        'longitude': f'{gps[0]}',
        'latitude': f'{gps[1]}',
        '距離': f'{distnace}',
    }
    table = str(datetime.today())[:11]
    result = firebase.post(f'/drive-manager-18863/{table}', data)
    prev_gps = gps
    print(i)
    time.sleep(1)



