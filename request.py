#! /usr/bin/env python3

import urllib.request
#read file output list of lines. removes endline characters. just because
def removeNewLine(string):
    return string.replace('\n','').replace('\r','')

#outputs a list of lines from a file
def readtxt(fileName):
    with open(fileName) as leFile:
        out=leFile.readlines()
    return list(map(removeNewLine,out))

apiKey = readtxt('apiKey')[0]
coords = readtxt('coords')[0]
config = readtxt('.config')
response = urllib.request.urlopen('https://api.forecast.io/forecast/'+apiKey+'49.2425468,-123.182896')

configSplit = [None]*len(config)
for x in range(len(config)):
    configSplit[x] = config[x].split(' = ')


