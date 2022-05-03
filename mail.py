import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail(address):
    email_user = 'b171325@rgukt.ac.in'
    email_password = 'asd123@#$'
    email_send = address

    subject = "QR Code for your Attendance!"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = f'Hi, find your QR code for attendance!<br>Cheers!'
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

send_mail("harvarnet@gmail.com")