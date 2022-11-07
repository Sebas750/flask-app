def sendWspMessage(text):
    from twilio.rest import Client 
    
    account_sid = 'ACfb5da8c1fbd6c6cb63e4b7b440e00719' 
    auth_token = '275e181f34867d7661c684ff0cd66ca4'

    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_= 'whatsapp:+14155238886', 
                                body= text,      
                                to = 'whatsapp:+56962452984' 
                            ) 
    