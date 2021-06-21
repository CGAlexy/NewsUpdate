#pip install secure-smtplib
import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    #created message and set its parameters
    msg = EmailMessage()
    msg.set_content(body)
    #can add or remove subject when needed
    msg['subject'] = subject
    msg['to'] = to

    #sets sender email and password
    user = "cgalexy1@gmail.com"
    msg['from'] = user
    password = "yfmczcnervpdowlt"

    #establishes connection to SMTP server and sends message
    server = smtplib.SMTP("smtp.gmail.com", 587)#587 is the SMTP port for sending emails
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
        email_alert("hey", "Testing", "2672709152@vtext.com")
#convert number to email here:
#https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/ 