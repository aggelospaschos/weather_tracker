# Weather App

This is a simple Flask web application that fetches current weather data from the OpenWeatherMap API based on user input.

## Project Overview

The Weather App allows users to retrieve weather information for a specific city by entering the city name into a form. The application then displays the current temperature and weather description for the provided city.

## Installation

Follow these steps to set up and run the Weather App on your local machine:

1. **Clone the Repository:**

`git clone https://github.com/aggelospaschos/weather_tracker.git`

2. **Install Dependencies:**

Navigate into the project directory and install the required Python dependencies:

`cd .../.../weather_tracker`

`pip install -r requirements.txt`

3. **Set Up Environment Variable:**

You need to set up an environment variable to store the OpenWeatherMap API key. You can do this by navigating to the `.env` file in the root directory of the project and adding the following line:

`OPENWEATHERMAP_API_KEY=your_api_key_here`

Replace `your_api_key_here` with your actual OpenWeatherMap API key.

## Running the App

Once you've completed the installation steps, you can run the Weather App locally:

1. **Run the Flask Application:**

`python script.py`

2. **Access the App:**
Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the Weather App. You can now enter a city name into the form and click "Get Weather" to retrieve weather information.

## Additional Notes

- If you don't have an OpenWeatherMap API key, you can sign up for a free account at [OpenWeatherMap](https://openweathermap.org/) to obtain one.
- Remember to keep your API key secure and never expose it publicly.
- For any issues or questions about the Weather App, please feel free to open an issue on the GitHub repository.

Enjoy using the Weather App!

