from firebase import firebase
import requests

firebase = firebase.FirebaseApplication('https://drive-manager-18863.firebaseio.com/', None)
print(firebase.get('/drive-manager-18863/', ''))

