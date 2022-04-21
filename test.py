from twilio.rest import Client

account_sid = 'ACc26a38a2609649a63cbd67130f12be4c'
auth_token = 'ff10a998a8c1cb3b0cdcc2bbb68e49af'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.☔",
                     from_='+14152376013',
                     to='+33638396077'
                 )

print(message.sid)