# Welcome to the Nope-ler Weather Tracker, utilizing React.js UI library and Flask WSGI server. 

# Setup:
1. Verify if your system is able to run Postgres. If so, continue to step 2. Otherwise, on line 5 of models.py, comment out the line reading " DATABASE = PostgresqlDatabase('weather_app') ", and directly above or below this line add:  " DATABASE = SqliteDatabase('weather.sqlite') "
2. In your terminal, create a Flask environment with the line: "virtualenv .env -p python3"; activate it with the code: "source .env/bin/actuvate".
3. Ensure all requirements have been installed with the line: "pip3 install -r requirements.txt".
4. Run your Flask WSGI: "python3 app.py".

# User Story:
1. User will register account to access weather
2. User will login to free account to access current and forecast weather in their selected location
3. User can create cities to track current and forecasted weather
4. User can click cities in order to see detailed weather information
5. User can edit/delete cities they no longer wish to track
6. User can logout

# Developed by:
1. Matt Welbourn https://www.linkedin.com/in/matt-welbourn-58ba6457,
2. Sam Liman https://www.linkedin.com/in/samliman,
3. and Yettsy Knapp https://www.linkedin.com/in/yettsy-jo-knapp

# GitHub Repositories:
1. Flask: https://github.com/mlwelbourn/Weather-Flask-App.git
2. React: https://github.com/yettsyjk/WeatherReactApp.git

(c) Matt Welbourn, Sam Liman, Yettsy Knapp. 2020
