#!/usr/bin/env python3

import argparse
import sys
import signal

from forwardshell import ForwardShell
from termcolor import colored

my_shell = None

def def_handler(sig, frame):
    global my_shell
    print(colored("\n\n[!] Quitting the program...\n", "red"))
    my_shell.remove_files()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    argparser = argparse.ArgumentParser(description="Forward Shell")
    argparser.add_argument("-u", "--url", dest="url", required=True, help="Main url. (Ex: 'http://url.com/index.php')")
    argparser.add_argument("-a", "--argument", dest="argument", required=True, help="Argument that execute commands. (Ex: 'cmd')")

    args = argparser.parse_args()

    return args.url, args.argument

def print_banner():
    print(colored("""
█▀▀ █▀█ █▀█ █░█░█ ▄▀█ █▀█ █▀▄ █▀ █░█ █▀▀ █░░ █░░
█▀░ █▄█ █▀▄ ▀▄▀▄▀ █▀█ █▀▄ █▄▀ ▄█ █▀█ ██▄ █▄▄ █▄▄\n""", 'white'))

    print(colored("""Mᴀᴅᴇ ʙʏ sᴀᴍᴍʏ-ᴜʟғʜ\n""", 'yellow'))

def main():
    global my_shell

    print_banner()
    url, argument = get_arguments()

    my_shell = ForwardShell(url, argument)
    my_shell.start()

if __name__ == "__main__":
    main()
