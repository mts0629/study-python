#!/usr/bin/env python

from urllib.request import urlopen

# Get UTC from 'worldtimeapi.org'
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())

# Send e-mail with SMTP
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
# 
# Beware the Ides of March.
# """)
# server.quit()
