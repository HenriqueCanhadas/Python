from twilio.rest import Client

account_sid = 'AC906fb314ba2d4000b78916ef36dab13d'
auth_token = 'd61f751b0989db1e918488c18a273d7e'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+19133694026',
  body='Oi Tudo bem?',
  to='+5511932738996'
)

print(message.sid)