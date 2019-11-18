from pyicloud import PyiCloudService
from two_way_auth import get_gps_from_iphone
import sqlite3
from cal_rho import get_distance
from firebase import firebase
api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

# 緯度経度をリストで保存
gps = get_gps_from_iphone(api)



conn = sqlite3.connect('gps_log.sqlite')
cur = conn.cursor()

path = './gps_log.sqlite3'

cur.execute('create table if not exists log(latitude INTEGER , longitude INTEGER )')
# cur.execute('delete from log')
cur.execute(f'INSERT INTO log VALUES (?, ?)', (gps[0], gps[1]))

cur.execute("select * from log")
cur.execute('select count(*) from log')
results = cur.fetchall()[0][0]

cur.execute('select * from log')


gps_list = [(float(i[0]), float(i[1])) for i in list(cur)]


distance = 0
if results >= 2:
    for i in range(0, results - 1):
        distance += get_distance(gps_list[i], gps_list[i + 1])
        print(distance)





print(distance)

# for row in cur:
#     print(row[0], row[1])


conn.commit()
conn.close()
