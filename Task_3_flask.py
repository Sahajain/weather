from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "77c78eb3dddab8df680ad3553101c3e3"

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json()
        return jsonify({
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        })
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
