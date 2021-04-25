import os
from twilio.rest import Client
account_sid = 'AC29ff7a8f1b129190d5c22baaf922056c'
auth_token = 'a135efbd53ade5a4a28bd57e75a75d03'
client = Client(account_sid, auth_token)
def send_sms(user_code,phone_number):
    message = client.messages.create(
        body= f'Hi! You user and verification code is {user_code}',
        from_ = '+15205829254',
        to = f'{phone_number}'

    )
    print(message.sid)