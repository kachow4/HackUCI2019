'''
Created on Feb 15, 2019
 
@author: dfa
'''
#yay first push
from pprint import pprint
import requests


import json

from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/", methods=['POST'])
def form_post():

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
    temp = ((cityfile['main']['temp'])-273.15)*(9/5)+32
    

    templatevars = {
        'city' : city,
        'cityinfo' : str(cityfile['weather'][0]['description']),
        'humidity': str(cityfile['main']['humidity']),
        'temp' : temp,
        } 
    return render_template('submit.html', templatevars=templatevars)
 
@app.route("/submit")
def submit():
    return render_template("submit.html")
 
if __name__=="__main__":
    app.run(debug=True)
    print(form_post.city)
