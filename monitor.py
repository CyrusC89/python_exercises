#!/usr/bin/env python
import os
import socket
import requests
import time


PORT = 25565 
HOST = 'localhost'
ENV_VARS = ['PUSHOVER_USER', 'PUSHOVER_TOKEN']
API_SERVER = 'https://api.pushover.net/1/messages.json'


def post(e):
    alert = {'token': os.environ.get('PUSHOVER_TOKEN'),
             'user': os.environ.get('PUSHOVER_USER'),
             'message': 'ERROR: %s' % e}

    r = requests.post(API_SERVER, data=alert)
    print r.status_code
    print r.text


def poller():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('test')
        s.close()
    except Exception as e:
        post(e)
        print "ERROR: %s" % e
        time.sleep(600)
    time.sleep(2.0)


def main():
    while True:
        poller()

if __name__ == '__main__':
    main()

