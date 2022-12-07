eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoicUZlU2ZwazJiMGlHdHZUTzMzQ0Z2WlhFYXBtc0poeGEiLCJleHAiOjE4MjgxMDI3MzYsImlhdCI6MTY3MDMzNjMzNiwianRpIjoiZWEyNzUwODItN2U5Ny00ZTEyLWE3YTMtYjFkYzk3MGExNGJlIn0.L1s6Q5mtUcCVidXukHhXnGneNAe3lADpEsyQ6fXr2ZI



Post
  # we use requests library for the samples
    import requests
    # session object
    session = requests.Session()
    # base url
    base_url = 'https://api.afromessage.com/api/send'
    # api token
    token = 'YOUR_TOKEN'
    # header
    headers = {'Authorization': 'Bearer ' + token}
    # request body
    body = {'callback': 'YOUR_CALLBACK',
            'from':' ',
            'sender':'YOUR_SENDER_NAME',
            'to': 'YOUR_RECIPIENT',
            'message': 'YOUR_MESSAGE'}
    # make request
    result = session.post(base_url, json=body, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print 'api success'
        else:
            # do failure
            print 'api error'
    else:
        # anything other than 200 goes here.
        print 'http error ... code: %d , msg: %s ' % (result.status_code, result.content)
                             


End::


Sms

    # we use requests library for the samples
    import requests
    # session object
    session = requests.Session()
    # base url
    base_url = 'https://api.afromessage.com/api/send'
    # api token
    token = 'YOUR_TOKEN'
    # header
    headers = {'Authorization': 'Bearer ' + token}
    # request parameters
    callback = 'YOUR_CALLBACK'
    to = 'YOUR_RECIPIENT'
    message = 'YOUR_MESSAGE'
    from = 'YOUR_IDENTIFIER_ID'
    sender = 'YOUR_SENDER_NAME'
    # final url
    url = '%s?from=%s&sender=%s,to=%s&message=%s&callback=%s' % (base_url,from,sender,to, message, callback)
    # make request
    result = session.get(url, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print 'api success'
        else:
            # do failure
            print 'api error'
    else:
        # anything other than 200 goes here.
        print 'http error ... code: %d , msg: %s ' % (result.status_code, result.content)
                                
SAMPLE SUCCESS RESULT
SAMPLE FAILURE RESULT

    {
        "acknowledge":"success",
        "response":{
            "status":"Send in progress...",
            "message_id":"9ab2867c-96ce-4405-b890-8d35d52c8e01",
            "message":"[YOUR_ORIGINAL_MESSAGE]",
            "to":"[ORIGINAL_RECIPIENT]"
        }
    }



                                
Send SMS (POST)

    # we use requests library for the samples
    import requests
    # session object
    session = requests.Session()
    # base url
    base_url = 'https://api.afromessage.com/api/send'
    # api token
    token = 'YOUR_TOKEN'
    # header
    headers = {'Authorization': 'Bearer ' + token}
    # request body
    body = {'callback': 'YOUR_CALLBACK',
            'from':'YOUR_IDENTIFIER_ID',
            'sender':'YOUR_SENDER_NAME',
            'to': 'YOUR_RECIPIENT',
            'message': 'YOUR_MESSAGE'}
    # make request
    result = session.post(base_url, json=body, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print 'api success'
        else:
            # do failure
            print 'api error'
    else:
        # anything other than 200 goes here.
        print 'http error ... code: %d , msg: %s ' % (result.status_code, result.content)
                                

Send Security Code

    
    # we use requests library for the samples
    import requests                            
    # session object
    session = requests.Session()
    # base url
    base_url = 'https://api.afromessage.com/api/challenge'
    # api token
    token = 'YOUR_TOKEN'
    # header
    headers = {'Authorization': 'Bearer ' + token}
    # request parameters
    callback = 'YOUR_CALLBACK'
    from = 'YOUR_IDENTIFIER_ID'
    sender = 'YOUR_SENDER_NAME'
    to = 'YOUR_RECIPIENT'
    pre = "YOUR_MESSAGE_PREFIX"
    post = "YOUR_MESSAGE_POSTFIX"
    sb = SPACES_BEFORE
    sa = SPACES_AFTER
    ttl = TIME_TO_LIVE
    len = CODE_LENGTH
    t = CODE_TYPE
    # final url
    url = '%s?from=%s&sender=%s&to=%s&pr=%s&ps=%s&callback=%s&sb=%d&sa=%d&ttl=%d&len=%d&t=%d' % (base_url, from, sender, to, pre, post, callback, sb, sa, ttl, len, t)
    # make request
    result = session.get(url, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print 'api success'
        else:
            # do failure
            print 'api error'
    else:
        # anything other than 200 goes here.
        print 'http error ... code: %d , msg: %s ' % (result.status_code, result.content)                                
The response contains two nodes acknowledge node and response node. Inspect the value of acknowledge to see if your request has secceeded or not. Below is a typical sample response object for this call.

A successful response object will contain, among other things, the code that's sent for the user, and a unique verification id that you can save for later use in the verification processs.

SAMPLE SUCCESS RESULT
SAMPLE FAILURE RESULT

    {   
        "acknowledge":"success",
        "response":
        {
                "status":"Send is in progress...",
                "message_id":"a3ddc51c-7ffe-4eaf-8ee1-a0c6628aaa2c",
                "message":"CUT32K is your verification code",
                "to":"+251999889988",
                "code":"CUT32K",
                "verificationId":"30748c9f-487c-4c82-a48b-4080ec00996c"
            }
    }
                                
Verify Code
 

    # we use requests library for the samples
    import requests
    # session configuration
    session = requests.Session()
    # base url
    base_url = 'https://api.afromessage.com/api/verify'
    # api token
    token = 'YOUR_TOKEN'
    # header
    headers = {'Authorization': 'Bearer ' + token}
    # request parameters
    # Note: You can also use the verification id sent in the challenge request. 
    # Use the `vc` query parameter to verify via verification id.
    to = 'YOUR_RECIPIENT'
    code = 'CODE_TO_VERIFY'
    # final url
    url = '%s?to=%s&code=%s' % (base_url, to, code)
    # make request
    result = session.get(url, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print 'api success'
        else:
            # do failure
            print 'api error'
    else:
        # anything other than 200 goes here.
        print 'http error ... code: %d , msg: %s ' % (result.status_code, result.content)
                                
The response contains two nodes acknowledge node and response node. Inspect the value of acknowledge to see if your request has secceeded or not. If verification is successful, we reply back with the entire verification object. Otherwise, we return a description of the verification error in the response.

SAMPLE SUCCESS RESULT
SAMPLE FAILURE RESULT

    {
        "acknowledge":"success",
        "response":{
            "phone":"+251999889988",
            "code":"854467",
            "verificationId":"95c9ac5f-3d67-4d93-95d5-5083814fd7d6",
            "sentAt":"1 minute ago"
        }
    }
                                
Pay us a visit on our social media accounts!
Terms & Conditions
Privacy Policy
Copyright © Afro Message

End::


   # we use requests library for the samples
    import requests
    # session configuration
    session = requests.Session()
    # base url
    base_url = 'https://api.afromessage.com/api/verify'
    # api token
    token = 'YOUR_TOKEN'
    # header
    headers = {'Authorization': 'Bearer ' + token}
    # request parameters
    # Note: You can also use the verification id sent in the challenge request. 
    # Use the `vc` query parameter to verify via verification id.
    to = 'YOUR_RECIPIENT'
    code = 'CODE_TO_VERIFY'
    # final url
    url = '%s?to=%s&code=%s' % (base_url, to, code)
    # make request
    result = session.get(url, headers=headers)
    # check result
    if result.status_code == 200:
        # request is success. inspect the json object for the value of `acknowledge`
        json = result.json()
        if json['acknowledge'] == 'success':
            # do success
            print 'api success'
        else:
            # do failure
            print 'api error'
    else:
        # anything other than 200 goes here.
        print 'http error ... code: %d , msg: %s ' % (result.status_code, result.content)

End::

