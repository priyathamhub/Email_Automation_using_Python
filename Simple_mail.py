# Python code to illustrate Sending mail from your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
#s.login("sender_mail","sender_password")
s.login("sender_mail@gmail.com", "sender_password")
# message to be sent 
message = "Hi, This message is sent from Python."

# sending the mail 
#s.sendmail("cc","bcc",message)
s.sendmail("reciever_mail@gmail.com", "bcc_mail@gmail.com", message) 

# terminating the session 
s.quit()

print("Message sent")
