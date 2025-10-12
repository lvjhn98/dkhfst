import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'template:dns-publish', 
            help='Save DNS entries to configuration file.'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/dns-publish.sh")