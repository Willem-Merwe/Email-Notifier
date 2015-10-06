import poplib
import time
from gi.repository import Notify

Notify.init("Email Notifier")

# POP3 Config
SERVER = "YOUR_MAIL_SERVER"
USER  = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

# connect to server
server = poplib.POP3(SERVER)

# login
server.user(USER)
server.pass_(PASSWORD)

# initiate counter
counter = server.stat()[0]

def getStat():
    return server.stat()[0]

while True:
    server = poplib.POP3(SERVER)
    server.user(USER)
    server.pass_(PASSWORD)
    
    if counter < getStat():
        counter = getStat()
        Notify.Notification.new("Check your mail").show()

