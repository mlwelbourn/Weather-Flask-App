# Project-3
Weather React/Flask App

# Setup:
1. Verify if your system is able to run Postgres. If so, continue to step 2. Otherwise, on line 5 of models.py, comment out the line reading " DATABASE = PostgresqlDatabase('weather_app') ", and directly above or below this line add:  " DATABASE = SqliteDatabase('weather.sqlite') "
2. In your terminal, create a Flask environment with the line: "virtualenv .env -p python3"; activate it with the code: "source .env/bin/actuvate".
3. Ensure all requirements have been installed with the line: "pip3 install -r requirements.txt".
4. Run your Flask WSGI: "python3 app.py".
