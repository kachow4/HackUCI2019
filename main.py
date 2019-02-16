'''
Created on Feb 15, 2019

@author: dfa
'''
#yay first push
from pprint import pprint
import requests
# city = input('Enter your travel destination: ')
# print(city)
# s = 'http://api.openweathermap.org/data/2.5/weather?q={c}&APPID=386aa376a85049b9a45c5fb223f1a691'.format(c=city)
# print(s)
# r = requests.get(s)
# cityfile = r.json()
# pprint(cityfile)
# print(cityfile['main']['temp_max'])
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=['POST'])
def form_post():
    fname = request.form['fname']
    lname = request.form['lname']
    city = request.form['city']
    s = 'http://api.openweathermap.org/data/2.5/weather?q={c}&APPID=386aa376a85049b9a45c5fb223f1a691'.format(c=city)
    r = requests.get(s)
    cityfile = r.json()
    pprint(cityfile)
#     print("hello")
    return "Hello "+fname+' '+lname+', in '+city+ ', the maximum temperature is '+str(cityfile['main']['temp_max'])

@app.route("/submit")
def submit():
    return render_template("submit.html")

if __name__=="__main__":
    app.run(debug=True)
