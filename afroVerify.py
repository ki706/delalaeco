# we use requests library for the samples
import requests
    # session configuration

   
session = requests.Session()
    # base url
base_url = 'https://api.afromessage.com/api/verify'
    # api token
token = 'eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoicUZlU2ZwazJiMGlHdHZUTzMzQ0Z2WlhFYXBtc0poeGEiLCJleHAiOjE4MjgxMDI3MzYsImlhdCI6MTY3MDMzNjMzNiwianRpIjoiZWEyNzUwODItN2U5Ny00ZTEyLWE3YTMtYjFkYzk3MGExNGJlIn0.L1s6Q5mtUcCVidXukHhXnGneNAe3lADpEsyQ6fXr2ZI'
    # header
headers = {'Authorization': 'Bearer ' + token}
    # request parameters
    # Note: You can also use the verification id sent in the challenge request. 
    # Use the `vc` query parameter to verify via verification id.
to = '0974273398'
code = '566303'
    # final url
url = '%s?to=%s&code=%s' % (base_url, to, code)
    # make request
result = session.get(url, headers=headers)
    # check result
if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            print(json['response'])
            # do success
            print ('api success')
        else:
            # do failure
            print ('api error')
else:
        # anything other than 200 goes here.
        print ('http error ... code: ')