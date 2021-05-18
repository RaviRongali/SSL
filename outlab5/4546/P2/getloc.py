#!/usr/bin/env python3

from datetime import datetime
import json
import requests


def response(name, **kwargs):
    return json.loads(requests.get('http://api.open-notify.org/{name}.json'.format(name=name), params=kwargs).text)


def iss_location():
    return response('iss-now')['iss_position']


def pass_time(longitude, latitude):
    # Returns (passing-time, (duration_minutes, duration_seconds))"
    data = response('iss-pass', lat=latitude, lon=longitude)['response'][0]
    return datetime.fromtimestamp(data['risetime']), divmod(data['duration'], 60)


def people_info():
    return [elem['name'] for elem in response('astros')['people']]


print('Current location of ISS:')
for k, v in iss_location().items():
    print('{k}: {v}'.format(k=k, v=v))

print('Enter Details to know when ISS will pass over a location:')
latitude = input('Latitude: ')
longitude = input('Longitude: ')
dtime, (mins, sec) = pass_time(longitude, latitude)
print('Date:', dtime.date())
print('Time:', dtime.time())
print('For: {mins} minutes and {sec} seconds'.format(mins=mins, sec=sec))

astros = people_info()
print('People currently in space:', len(astros))
for num, name in enumerate(astros, 1):
    print('{num}. {n}'.format(num=num, n=name))
