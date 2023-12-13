from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


def get_day_number():
  return datetime.now().timetuple().tm_yday


def get_christmas_day():
  current_year = datetime.now().year
  if current_year % 4 != 0:
    return 365 - 6
  elif current_year % 100 != 0:
    return 366 - 6
  elif current_year % 400 == 0:
    return 366 - 6
  else:
    return 365 - 6


def get_current_hour():
  return datetime.now().hour


def get_current_minute():
  return datetime.now().minute


def get_current_second():
  return datetime.now().second


@app.route('/live-counter')
def live_counter():
  day_number = get_day_number()
  christmas_day = get_christmas_day()
  days_left = christmas_day - day_number - 1
  hours_left = 24 - get_current_hour() - 1
  minutes_left = 60 - get_current_minute() - 1
  seconds_left = 60 - get_current_second()
  if minutes_left < 0:
    minutes_left += 60
    hours_left -= 1
  if hours_left < 0:
    hours_left += 24
    days_left -= 1
  if days_left < 0:
    days_left = 0
    hours_left = 0
    minutes_left = 0
    seconds_left = 0
  return f"{days_left} day(s) {hours_left} hour(s) {minutes_left} minute(s) {seconds_left} second(s) left until Christmas day"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
