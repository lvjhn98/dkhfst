import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'template:ip-list', 
            help='Show IPs of services of the current project.'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/ip-list.sh" + " ".join(sys.argv[2:]))