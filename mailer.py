import re
from flask import Flask, request
from datetime import date
from datetime import datetime
from time import sleep
import time
from flask_cors import CORS
import requests
import smtplib

app=Flask(__name__)
CORS(app)

@app.route('/' , methods=["GET", "POST"])
def hello():
    def mailer(msg):
        print("finction called")
        user='b171325@rgukt.ac.in'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user,'asd123@#$')
        print("sending mail")
        message = "Test Mail from HTML" + msg
        server.sendmail(user,'harshavardhang123@gmail.com',message)
        print("mail sent")
        server.quit()
        return "mail sent"
    op = request.get_json()
    #email = request.form["email"]
    print(op)
    mailer(op)
    print("mailing0")
    return "Done"

if __name__ == '__main__':
    app.run(debug=True)