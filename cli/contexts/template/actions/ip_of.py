import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'template:ip-of', 
            help='Show IP of a specific service of the current project.'
        )
    action.add_argument(
        'service', 
        type=str, 
        help='Name of service to display IP of.'
    )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/ip-of.sh " + " ".join(sys.argv[2:]))