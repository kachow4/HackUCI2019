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
                break
        except:
            print('error')
            pass
    if cityid == None:
        return 'no id found'
    s = 'http://api.openweathermap.org/data/2.5/weather?q={c}&APPID=386aa376a85049b9a45c5fb223f1a691'.format(c=city)
    r = requests.get(s)
    cityfile = r.json()
#     pprint(cityfile)
    temp = ((cityfile['main']['temp'])-273.15)
    cloudcover = (cityfile['clouds']['all'])
    description = cityfile['weather'][0]['description']
    ''''''
    essentials = '''\
Chapstick
Vitamins
Meds
Pain reliever pills
Wallet
Casual watch
House key
Reading glasses
Sunglasses
Ear plugs
Eye mask
Book
Camera
Cell phone
Cell phone charger
Boarding pass
Printed trip itinerary
Hand sanitizer'''
    essentials = essentials.split('\n')
    clotheslist = [] 
    if 'rain' in description:
        clotheslist.extend([item for item in ['umbrella', 'raincoat', 'rain boots']])
    if 'clouds' in description:
        clotheslist.extend([item for item in ['hoodie', 'jacket', 'coat']])
    if 'sun' in description:
        clotheslist.extend([item for item in ['sun screen', 'hat', 'light jacket']])
    if 'wind' in description:
        clotheslist.extend([item for item in ['wind breaker', 'Vaseline', 'scarf', 'allergy medication']])
    if 'snow' in description:
        clotheslist.extend([item for item in ['down jacket', 'beanie', 'mittens', 'warm boots', 'snow boots', 'scarf', 'snow pants', 'hand-warmers']])
    if 'clear' in description:
        if temp < 18:
            clotheslist.extend([item for item in ['jacket']])
        else:
            clotheslist.append('light jacket')
    if 'breeze' in description:
        clotheslist.extend([item for item in ['wind breaker', 'scarf', 'hat']])
    
    if temp > 0:
        if temp < 4:
            clotheslist.extend([item for item in ['beanie', 'down jacket', 'mittens', 'warm boots', 'scarf', 'hand-warmers'] if item not in clotheslist])
        elif temp < 18:
            clotheslist.extend([item for item in ['hoodie', 'jacket', 'hat'] if item not in clotheslist])
        elif temp < 30:
            clotheslist.extend([item for item in ['hat', 'sunglasses', 'light jacket'] if item not in clotheslist])
        else:
            clotheslist.extend([item for item in ['hat', 'sunglasses', 'personal fan', 'aloe vera'] if item not in clotheslist])
    
    
    
    ''''''
    templatevars = {
        'city' : city,
        'description' : description,
        'humidity': str(cityfile['main']['humidity']),
        'temp' : temp,
        'cloudcover':cloudcover,
        'essentials' : essentials,
        'clotheslist' : clotheslist,
        } 
    return render_template('submit.html', templatevars=templatevars)
 
@app.route("/submit")
def submit():
    return render_template("submit.html")
 
if __name__=="__main__":
    app.run(debug=True)
    print(form_post.city)
