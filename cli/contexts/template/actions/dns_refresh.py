import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser('template:dns-refresh', help='Refresh DNS configuration.')
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/dns-refresh.sh")