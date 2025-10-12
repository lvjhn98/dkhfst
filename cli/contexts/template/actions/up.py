import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'template:up', 
            help='Run template related services (DNS, networks, etc.).'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/up.sh")