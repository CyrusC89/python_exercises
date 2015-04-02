#!/usr/bin/env python

# DRY: DO NOT repeat yourself
import requests

def compare_status(status):
   print status


def main():
    r = requests.get("http://www.google.com")
    status_code = r.status_code
    compare_status(status_code)
    


if __name__ == '__main__':
    main()
