import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'template:dns-update', 
            help='Publish and refresh DNS entries.'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/dns-update.sh")