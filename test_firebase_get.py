from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://drive-manager-18863.firebaseio.com/', None)
all_firevase_data = firebase.get('/drive-manager-18863/', '')
print(type(all_firevase_data))
print(all_firevase_data['2019-11-18 '])
