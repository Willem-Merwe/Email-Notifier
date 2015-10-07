__author__ = 'Riogan'

import poplib
import email
import time
from gi.Repository import Notify

Notify.init("Email Notifier")

# POP3 Config
SERVER = "mail.dragons-end.co.za"
USER  = "riogan@dragons-end.co.za"
PASSWORD = "Badger86"

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

    time.sleep(5)
