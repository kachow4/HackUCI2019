'''
Created on Feb 15, 2019
 
@author: dfa
'''
#yay first push
from pprint import pprint
import requests
import json
import math
from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/", methods=['POST'])
def form_post():

    cityid = None
    city = request.form['city']
    triplen = int(request.form['date'])
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
    pprint(cityfile)
    temp = float(str((cityfile['main']['temp'])-273.15)[:4])
    cloudcover = (cityfile['clouds']['all'])
    description = cityfile['weather'][0]['description']
    genweather = cityfile['weather'][0]['main']
    ''''''
    essentials = '''\
Chapstick
Vitamins
Meds
Pain reliever pills
Wallet
Casual watch
House key
Glasses
Sunglasses
Ear plugs
Eye mask
Book
Camera
Cell phone
Cell phone charger
Boarding pass
Printed trip itinerary
Hand sanitizer
Appropriate currency'''
    
    toiletries = """\
Contact solution
Perfume
Nail clippers
Tweezers
Makeup
Toothbrush
Toothpaste
Hairbrush
Floss
Deodorant
Shaver
Shaving cream/gel
Contacts
Q-tips"""
    essentials = essentials.split('\n')
    toiletries = toiletries.split('\n')
    packbyweather = [] 
    if 'rain' in description:
        packbyweather.extend([item for item in ['Umbrella', 'Raincoat', 'Rain boots']])
    if 'clouds' in description:
        packbyweather.extend([item for item in ['Hoodie', 'Jacket', 'Coat']])
    if 'sun' in description:
        packbyweather.extend([item for item in ['Sun screen', 'Hat', 'Light Jacket']])
    if 'wind' in description:
        packbyweather.extend([item for item in ['Wind Breaker', 'Vaseline', 'Scarf', 'Allergy Medication']])
    if 'snow' in description:
        packbyweather.extend([item for item in ['Thick Jacket', 'Beanie', 'Mittens', 'Warm boots', 'Snow boots', 'Scarf', 'Snow pants', 'Hand-warmers', 'Long underwear']])
    if 'clear' in description:
        if temp < 18:
            packbyweather.extend([item for item in ['Jacket']])
        else:
            packbyweather.append('Light Jacket')
    if 'breeze' in description:
        packbyweather.extend([item for item in ['Wind Breaker', 'Scarf', 'Hat']])
    
    if temp > 0:
        if temp < 4:
            packbyweather.extend([item for item in ['Beanie', 'Thick Jacket', 'Mittens', 'Warm boots', 'Scarf', 'Hand-warmers'] if item not in packbyweather])
        elif temp < 18:
            packbyweather.extend([item for item in ['Hoodie', 'Jacket', 'Hat'] if item not in packbyweather])
        elif temp < 30:
            packbyweather.extend([item for item in ['Hat', 'Sunglasses', 'Light Jacket'] if item not in packbyweather])
        else:
            packbyweather.extend([item for item in ['Hat', 'Sunglasses', 'Personal fan', 'Aloe Vera'] if item not in packbyweather])
    
    ##############################
    regclothes = ['sets of underwear', 'pairs of socks', 'casual shirts', 'pairs of pants', 'belt', 'set of pajamas']
    quantityclothes = []
    for item in regclothes:
        if 'underwear' in item or 'socks' in item:
            quantityclothes.append(str(triplen+1)+' '+item)
        elif 'shirts' in item:             
            if triplen > 10:
                quantityclothes.append(str(math.ceil(triplen/2)+2)+' '+item)
            elif triplen >= 5:
                quantityclothes.append(str(triplen-2)+' '+item)
            else:
                quantityclothes.append(str(triplen)+' '+item)
        elif 'pants' in item:
            quantityclothes.append(str(math.ceil(triplen/2))+' '+item)
        else:
            quantityclothes.append('1 '+item)
#     print(quantityclothes)
        
    
    
    ''''''
    templatevars = {
        'city' : city,
        'description' : description,
        'humidity': str(cityfile['main']['humidity']),
        'temp' : temp,
        'cloudcover':cloudcover,
        'essentials' : essentials,
        'toiletries' : toiletries,
        'packbyweather' : packbyweather,
        'quantityclothes' : quantityclothes,
        'genweather' : genweather,
        } 
    return render_template('submit.html', templatevars=templatevars)
 
@app.route("/submit")
def submit():
    return render_template("submit.html")
 
if __name__=="__main__":
    app.run(debug=True)
    print(form_post.city)
