import urllib2
import json


api = '4850b2b194bae5d077e048d768aebb840a9c07f4'

url = 'https://api.locu.com/v1_0/venue/search/?'


local = 'Newport Beach'
locality = local.replace(' ', '%20')


new_url = url + 'api_key=' + api + '&locality=' + locality


obj = urllib2.urlopen(new_url)
data = json.load(obj)