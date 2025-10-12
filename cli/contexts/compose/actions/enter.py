import os 
import sys

def action(parser): 
    action = \
        parser.add_parser(
            'compose:enter', 
            help='Enter a container in the project.'
        )
    action.add_argument(
        'service', 
        type=str, 
        help='Name of the service to enter.'
    )
    action.set_defaults(func=handle)


def handle(args):
    os.system("bash ./scripts/project/enter.sh " + " ".join(sys.argv[2:]))