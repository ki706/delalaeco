import requests
session = requests.Session()
# base url
base_url = 'https://api.afromessage.com/api/send'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoicUZlU2ZwazJiMGlHdHZUTzMzQ0Z2WlhFYXBtc0poeGEiLCJleHAiOjE4MjgxMDI3MzYsImlhdCI6MTY3MDMzNjMzNiwianRpIjoiZWEyNzUwODItN2U5Ny00ZTEyLWE3YTMtYjFkYzk3MGExNGJlIn0.L1s6Q5mtUcCVidXukHhXnGneNAe3lADpEsyQ6fXr2ZI'

# session object

# api token
#token = 'YOUR_TOKEN'
    # header
headers = {'Authorization': 'Bearer ' + token}
    # request body
body = {'callback': '',
            'from':'',
            'sender':'',
            'to': '0974273398',
            'message': 'Test123  '}
    # make request
result = session.post(base_url, json=body, headers=headers)
print(result)
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
        print ('NNNNNNNoooooooooooooooooooooo')