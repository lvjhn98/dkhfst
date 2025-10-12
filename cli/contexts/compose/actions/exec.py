import os 
import sys
import argparse

def action(parser): 
    action = \
        parser.add_parser(
            'compose:exec', 
            help='Execute a script in a container in the project.'
        )
    action.add_argument(
        'service', type=str, help='Name of the service to execute a script in the container.'
    )
    action.add_argument(
        'command', 
        nargs=argparse.REMAINDER, 
        type=str, help='Command to execute.'
    )
    action.set_defaults(func=handle)


def handle(args):
    os.system("bash ./scripts/project/exec.sh " + " ".join(sys.argv[2:]))