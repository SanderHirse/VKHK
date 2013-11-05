import json
import os

firstname = raw_input('Enter your firstname: ')
lastname = raw_input('Enter your lastname: ')

firstname = firstname.lower();
data = [{ 'firstname':firstname, 'lastname':lastname} ]

data_string = json.dumps(data)

with open('database/'+firstname+".json","w+") as f:
   	f.write(data_string)
   	f.close() 

users = json.loads(open('database/'+firstname+'.json').read())

for user in users:
   print 'Welcome ' + user['firstname'].capitalize()
