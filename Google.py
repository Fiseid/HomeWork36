import requests



KEY = ''

url = 'https://maps.googleapis.com/maps/api/geocode/'

output_format = 'json'

addr_str = '49.589938, 34.550938'

full_addr = url + output_format + '?address=' + addr_str + '&key=' + KEY

response = requests.get(full_addr)

#-----------------------------------------------------------------------

#params = {'latlng': '49.589938, 34.550938', 'key': ''}

#response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)