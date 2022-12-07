
import requests                            
    # session object
session = requests.Session()
    # base url
base_url = 'https://api.afromessage.com/api/challenge'
    # api token
token = 'eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoicUZlU2ZwazJiMGlHdHZUTzMzQ0Z2WlhFYXBtc0poeGEiLCJleHAiOjE4MjgxMDI3MzYsImlhdCI6MTY3MDMzNjMzNiwianRpIjoiZWEyNzUwODItN2U5Ny00ZTEyLWE3YTMtYjFkYzk3MGExNGJlIn0.L1s6Q5mtUcCVidXukHhXnGneNAe3lADpEsyQ6fXr2ZI'
    # header
headers = {'Authorization': 'Bearer ' + token}
    # request parameters
callback = ''
fromm = ''
sender = ''
to = '0974273398'
pre = ""  
post = " is your Z-dealer verification code."
sb = 0
sa = 0
ttl = 0
len = 6
t = 0
    # final url
url = '%s?from=%s&sender=%s&to=%s&pr=%s&ps=%s&callback=%s&sb=%d&sa=%d&ttl=%d&len=%d&t=%d' % (base_url, fromm, sender, to, pre, post, callback, sb, sa, ttl, len, t)
    # make request
result = session.get(url, headers=headers)
    # check result
if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print(json['response'])
            print ('api success')
        else:
            # do failure
            print ('api error')
else:
        # anything other than 200 goes here.
        print ('http error ... ')