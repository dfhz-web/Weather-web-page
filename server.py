from flask import Flask, render_template, request
from  weather import get_current_weather
from waitress import serve

# from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index') 
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    #this if helps if the cx sends empyt spaces, or nothing
    if not bool(city.strip()):
       return render_template('city_no_found.html')
    weather = get_current_weather(city)


   #City is not found by API
    if not weather['cod'] == 200:
        return render_template('city_no_found.html')

    return render_template(
        "weather.html",
        title= weather['name'],  
        status= weather['weather'][0]['description'].capitalize(),
        temp=f"{weather['main']['temp']:.1f}",
        feels_like=f"{weather['main']['feels_like']:.1f}"
     )

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    #server is from the waitress module to run the flask application 
    serve(app, host="0.0.0.0", port=8000)
    