#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
import sys

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(dir, min_percent):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(dir)
    du_free_percent = 100*du.free/du.total
    return du_free_percent > min_percent

def check_localhost():
    """check localhost is correctly configured on 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

if check_cpu_usage():
    error_message = "CPU usage is over 80%"
elif not check_disk_usage('/',20):
    error_message = "Available disk space is less than 20%"
elif not check_localhost():
    error_message = "localhost cannot be resolved to 127.0.0.1"
else:
    pass

# send email if any error reported
if __name__ == "__main__":
    try:
        sender = "madhavan2rm@gmail.com"
        receiver = "18s022@gmail.com"
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
    except NameError:
        pass

