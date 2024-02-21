import os
from flask import Flask, render_template, request
import requests

# Create a Flask application instance
app = Flask(__name__)

# API key for accessing OpenWeatherMap API
api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city):
    if not api_key:
        print("OpenWeatherMap API key not found.")
        return None

    # API endpoint URL for current weather data by city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        # Send GET request to the API endpoint
        response = requests.get(url)

        # Raise an exception for any HTTP error
        response.raise_for_status()

        # Parse JSON response into a Python dictionary
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions, such as network errors
        print("Error fetching weather data:", e)
        return None

# Route for the homepage ("/")
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # If the request method is POST, it means the form has been submitted
        # Get the city input from the form
        city = request.form['city']
    else:
        # If the request method is GET, set default city to New York
        city = "New York"

    # Fetch weather data for the specified city
    weather_data = get_weather_data(city)
    if weather_data:
        # If weather data is successfully fetched, render the index.html template with the weather data
        return render_template('index.html', weather_data=weather_data)
    else:
        # If fetching weather data fails, return an error message
        return "Failed to fetch weather data. Please try again later."

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode to see detailed error messages during development
