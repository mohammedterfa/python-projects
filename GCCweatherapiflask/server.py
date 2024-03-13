from flask import Flask, request
from flask_restx import Resource, Api
from weather import get_current_weather

app = Flask(__name__)
api = Api(app)


@api.route('/<string:city>')
class CityWeather(Resource):

    def post(self, city):
        city = request.args.get('city')

        weather_data = get_current_weather(city)

        #City is not found by API
        if not weather_data['cod'] == 200:
            return {"msg": "لم يتم العثور على المدينة"}

        return {"title": weather_data["name"],
                "status": weather_data["weather"][0]["description"].capitalize(),
                "temp" : f"{weather_data['main']['temp']:.1f}",
                "feels_like" :  f"{weather_data['main']['feels_like']:.1f}"}
            
        

if __name__ == '__main__':
    app.run(debug=True)