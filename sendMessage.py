from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd81896b6368881926ee1420be8c3f6b0"
auth_token  = "cf5302b43196f38d84dc68b8b1dda053"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Nhaaa please?! I test you <3",
    to="+5581992188994",    # Replace with your phone number
    from_="+551530420593") # Replace with your Twilio number
print message.sid