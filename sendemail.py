import smtplib 
from_addr = '' 
to_addr  = 'david@yahoo.com' 
subject='Lab Test'
from_name='Javoun'
to_name='me'
msg='Lets see if it works.'
message = """
From: {} <{}> 
To: {} <{}> 
Subject: {} 

{} 
""" 
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials (if needed) 
username = '' 
password = '{}' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 