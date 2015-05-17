#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:06:47 2015

@author: omancarci
"""
import RPi.GPIO as GPIO
import configparser
import forecastio
import time

# function to interact with forecast.io
def takeUmbrella(apiKey, lattitude, longitude):
    forecast = forecastio.load_forecast(apiKey, lattitude, longitude, units = 'si')
    now = forecast.currently().precipProbability>0.5
    today = forecast.daily().data[0].precipProbability > 0.4    
    return {'rainNow' : now, 'rainLater': today}


# read configuration file
config = configparser.ConfigParser()
config.read('.config')
rainNowOut = int(config['piConfig']['rainNowOut'])
rainLaterOut = int(config['piConfig']['rainLaterOut'])
apiKey = config['forecast.io']['apiKey']
lattitude = float(config['forecast.io']['lattitude'])
longitude = float(config['forecast.io']['longitude'])

# setup GPIO outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(rainNowOut, GPIO.OUT)
GPIO.setup(rainLaterOut, GPIO.OUT)

# blink once on startup
GPIO.output(rainNowOut, GPIO.HIGH)
GPIO.output(rainLaterOut, GPIO.HIGH)
time.sleep(5)
GPIO.output(rainNowOut, GPIO.LOW)
GPIO.output(rainLaterOut, GPIO.LOW)

try:
    while True:
        umbrella = takeUmbrella(apiKey, lattitude, longitude)
        GPIO.output(rainNowOut, umbrella['rainNow'])
        GPIO.output(rainLaterOut, umbrella['rainLater'])
        # sleep is in a for loop to make in interruptible
        for i in range(60*30):
            time.sleep(1)
except KeyboardInterrupt:
    # clean exit on interrupt
    GPIO.cleanup()
