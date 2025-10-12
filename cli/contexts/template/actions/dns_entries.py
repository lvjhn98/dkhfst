import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'template:dns-entries', 
            help='Get raw DNS entries for DNSMasq.'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/dns-entries.sh")