import json
filename='users.json'
users = {'first':['Adam','John'], 'last':['Johnson', 'Adams'], 'age':['39', '27'],'city':['Chicago', 'Louisville']}
with open(filename, 'w') as l:
    json.dump(users, l)