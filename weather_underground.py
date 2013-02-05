import urllib2
import urllib
import json

API_Key = ""

BASE_PATH = "http://api.wunderground.com/api/" + API_Key + "/conditions/q/19104.json"

f = urllib2.urlopen(BASE_PATH)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['current_observation']['display_location']['city']
temp = parsed_json['current_observation']['temp_c']
print "Current temperature in %s is: %s" % (location, temp)
f.close()