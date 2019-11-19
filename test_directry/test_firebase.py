'''
pythonでfirebase
参考URL：https://www.youtube.com/watch?v=rKuGCQda_Qo
'''
from datetime import datetime
from firebase import firebase

firebase = firebase.FirebaseApplication('https://drive-manager-18863.firebaseio.com/', None)
data = {
    '目的地': '市役所',
    '仕事内容': 'MTG',
    'longitude': '39.122',
    'latitude': '140.02',
}
table = str(datetime.today())[:11]

result = firebase.post(f'/drive-manager-18863/{table}', data)
print(result)

