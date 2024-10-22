from flask import  Flask, render_template, request, redirect, url_for
from dotenv import  load_dotenv
import os 
import  requests
from weather import get_current_weather
from waitress  import serve


app  = Flask(__name__)

@app.route('/')
@app.route('/home')
def home ():
    weather_data=  get_current_weather()
    return render_template(
        "home.html",
        city = weather_data['name'],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


@app.route('/weather')
def  weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = 'tehran'
    weather_data=  get_current_weather(city)
    if  not weather_data ['cod'] == 200 :
        return redirect(url_for('not_found'))
    
    return render_template(
        "weather.html",
        city = weather_data['name'],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


@app.route('/NotFound')
def  not_found():
    weather_data=  get_current_weather()
    return render_template(
        "404.html",
        city = weather_data['name'],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if  __name__ == '__main__':
    serve(app , host='0.0.0.0', port=5000) 

