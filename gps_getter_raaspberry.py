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
distance = 0

firebase = firebase.FirebaseApplication('https://drive-manager-18863.firebaseio.com/', None)
all_firevase_data = firebase.get('/drive-manager-18863/', '')
if all_firevase_data != None:
    date_list = all_firevase_data.keys()
else:
    date_list = {}
date = str(datetime.today())[:11]
koutei = 1
if date not in date_list:
    koutei = 0
    with open('koutei.txt', 'w') as f:
        print(str(koutei), file=f)

else:
    with open('koutei.txt') as f:
        koutei = str(int(f.read()) + 1)

    with open('koutei.txt', 'w') as f:
        print(str(koutei), file=f)

table1 = f"{date}/行程{koutei}/目的地：{'市役所'}/内容：{'MTG'}"
data = {
    '合計距離': distance

}

result = firebase.post(f'/drive-manager-18863/{table1}',data)
total = list(firebase.get(f'/drive-manager-18863/{table1}', ""))[0]
print(total)

for i in range(5):

    gps = get_gps_from_iphone(api)
    if prev_gps != ():
        distance += get_distance(prev_gps, gps)
    firebase.put(f'/drive-manager-18863/{table1}/total','合計距離',distance)
    prev_gps = gps
    print(i)

    time.sleep(1)
