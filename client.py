#!/usr/bin/python

# Allow using the `socket` library
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5000))

def dump_proc_self_maps():
    """Prints the output of the server's /proc/self/maps"""
    return

def server_exit():
    """Forces the server to print 'Hello, world!'"""
    return

def rop():
    """Crashes the server using a stack-smashing attack"""
    return

