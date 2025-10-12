import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser('template:logs', help='Show logs for template related services.')
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/logs.sh" + " ".join(sys.argv[2:]))