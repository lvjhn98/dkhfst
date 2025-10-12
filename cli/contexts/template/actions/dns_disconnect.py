import os

def action(parser): 
    action = \
        parser.add_parser(
            "template:dns-disconnect", 
            help="Disconnect the current DNS from the current project's network."
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/dns-disconnect.sh")