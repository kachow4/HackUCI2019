'''
Created on Feb 15, 2019
 
@author: dfa
'''
#yay first push
from pprint import pprint
import requests
<<<<<<< Updated upstream
city = input('Enter your travel destination: ')
print(city)
s = 'http://api.openweathermap.org/data/2.5/weather?q={c}&APPID=386aa376a85049b9a45c5fb223f1a691'.format(c=city)
print(s)
r = requests.get(s)
cityfile = r.json()
pprint(cityfile)
print(cityfile['main']['temp_max'])
=======
import json
# city = input('Enter your travel destination: ')
# print(city)
# s = 'http://api.openweathermap.org/data/2.5/weather?q={c}&APPID=386aa376a85049b9a45c5fb223f1a691'.format(c=city)
# print(s)
# r = requests.get(s)
# cityfile = r.json()
# pprint(cityfile)
# print(cityfile['main']['temp_max'])
>>>>>>> Stashed changes
from flask import Flask, render_template, request
# from Tools.scripts.parse_html5_entities import fname
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/", methods=['POST'])
def form_post():
<<<<<<< Updated upstream
    cityid = None
    city = request.form['city']
    with open('city.list.json/city.list.json', encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            pass
    datalist =  []   
    for i in data:
        try:
            datalist.append((i['name'], i['id']))
        except:
            pass
        
    
    for x in datalist:
        try:
            if x[0] == city:
                cityid = x[1]
        except:
            print('error')
            pass
    if cityid == None:
        return 'no id found'
    s = 'http://api.openweathermap.org/data/2.5/weather?q={c}&APPID=386aa376a85049b9a45c5fb223f1a691'.format(c=city)
    r = requests.get(s)
    cityfile = r.json()
    pprint(cityfile)
    templatevars = {
        'cityinfo' : str(cityfile['list'][0]['weather']),
        'fname' : fname,
        'lname' : lname
        } 
    return render_template('submit.html', templatevars=templatevars)
 
@app.route("/submit")
def submit():
    return render_template("submit.html")
 
if __name__=="__main__":
    app.run(debug=True)
    print(form_post.city)
