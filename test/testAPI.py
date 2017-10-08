# import requests
# import json
#
# resp = requests.get('https://api.github.com/users/showkat2203/following')
# if resp.status_code != 200:
#     resp.raise_for_status()
# print(resp.status_code)
# print(resp.json())
# hello = resp.json()
# print (json.dumps(hello))

import urllib3
import facebook
import requests


token = "EAACEdEose0fD30gd3k9HZCjB2qmFlTQlh71aCcFNaCe96KRYqEYUEivQ9yAMwgy" \
        "YCbD0ZD"

graph = facebook.GraphAPI(access_token=token, version = 2.7)
# events = graph.request('/search?q=Poetry&type=event&limit=10000')
events = graph.request('1533630466950906/events')

print (events)
print (events['data'])

# fp = open('/tmp/bengali', 'w+')
data = events['data'][0]['description']
print type(data)
print (data.encode('utf-8'))

# fp.write(data.encode('utf-8'))
# fp.flush()
# eventList = events['id']
#
# print (eventList)
#
# # eventid = eventList[1]['id']
#
# eventid = eventList
#
# event1 = graph.get_object(id=eventid,fields='attending_count,can_guests_invite,category,cover,declined_count,description,end_time,guest_list_enabled,interested_count,'
#         'is_canceled,is_page_owned,is_viewer_admin,maybe_count,noreply_count,owner,parent_group,place,ticket_uri,timezone,type,updated_time')
# attenderscount = event1['attending_count']
# declinerscount = event1['declined_count']
# interestedcount = event1['interested_count']
# maybecount = event1['maybe_count']
# noreplycount = event1['noreply_count']

#
# attenders = requests.get("https://graph.facebook.com/v2.7/"+eventid+"/attending?access_token="+token+"&limit="+str(attenderscount))
# attenders_json = attenders.json()
#
# #print (attenders_json)
#
#
# admins = requests.get("https://graph.facebook.com/v2.7/"+eventid+"/admins?access_token="+token)
# admins_json = admins.json()
# print (admins_json)
