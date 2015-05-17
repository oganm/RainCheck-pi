# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:42:24 2015

@author: omancarci
"""

#! /usr/bin/env python3
import configparser

config = configparser.ConfigParser()

config['forecast.io'] = {'apiKey': '',
                         'lattitude': '',
                         'longitude': ''}

config['piConfig'] = {'rainNowOut' : '',
                      'rainLaterOut' : ''}                       
with open(".config",'w') as configFile:
    config.write(configFile)