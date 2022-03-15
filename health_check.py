#!/usr/bin/env python3

from emails import generate_email, send_email
import os
import psutil
import shutil

def check_cpu():
    '''Devuelve False si el uso de CPU es > 80%'''
    print('CPU-usage')
    print('{}%\n\n'.format(psutil.cpu_percent(2)))
    return psutil.cpu_percent(2) < 80

def check_disk():
    '''Devuelve False si el disco disponible es < 20%'''
    usage = shutil.disk_usage('/')
    free = usage[2]
    total = usage[0]
    print('Available disk')
    print('{}%\n\n'.format(free / total * 100))
    return free / total > 0.2

def check_memory():
    '''Devuelve False si la memoria disponible es < 500MB'''
    ram_available_bytes = psutil.virtual_memory()[1]
    # Return in MBs
    ram = ram_available_bytes / (1024 ** 2)
    print('Available RAM')
    print('{} MBs\n\n'.format(ram))
    return ram > 500

def check_network():
    '''Devuelve False si no puede resolver la dirección ip'''
    ip = '127.0.0.1'
    network_ok = os.system('ping -c 5 {} > /dev/null;'.format(ip)) is 0
    print('Network')
    print('{} reached: {}\n\n'.format(ip, network_ok))
    return network_ok

def notify(asunto):
    email_from = 'automation@example.com'
    email_to = 'student-02-2fcef9f5ba3b@example.com'
    email_subject = asunto
    email_body = 'Please check your system and resolve the issue as soon as possible.'

    msg = generate_email(email_from, email_to, email_subject, email_body, '')
    send_email(msg)

def main():
    if not check_cpu():
        notify('Error - CPU usage is over 80%')
    if not check_disk():
        notify('Error - Available disk space is less than 20%')
    if not check_memory():
        notify('Error - Available memory is less than 500MB')
    if not check_network():
        notify('Error - localhost cannot be resolved to 127.0.0.1')

main()
