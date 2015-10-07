__author__ = 'riogan'

import ConfigParser
import email
import poplib
import os.path
import sys
from gi.repository import Notify

def readMailConfig(configfile):
    config = ConfigParser.RawConfigParser()
    config.read(configfile)
    
    mail_server = config.get('general','SERVER')
    mail_username = config.get('general', 'USERNAME')
    mail_password = config.get('general', 'PASSWORD')
    
    return (mail_server, mail_username, mail_password)

def readMessage(host, user, key):
    server = poplib.POP3(host)
    server.user(user)
    server.pass_(key)
    Notify.init("Email Notifier")
    (numMsgs, totalSize) = server.stat()
    if numMsgs == 0:

        Notify.Notification.new('No new Emails received. Shuting down..').show()
    else:
        Notify.Notification.new(('You have {} new emails.').format(numMsgs)).show()

if __name__ == '__main__':
	test = os.path.dirname(os.path.abspath(sys.argv[0]))
    	test = os.path.join(test, "config.ini")
	
	mail=readMailConfig(test)
	readMessage(mail[0], mail[1], mail[2])
