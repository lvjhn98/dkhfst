import os

def action(parser): 
    action = \
        parser.add_parser(
            "template:dns-connect", 
            help="Connect the current DNS to the current project's network."
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/dns-connect.sh")