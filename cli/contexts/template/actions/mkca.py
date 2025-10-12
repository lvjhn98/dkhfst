import os 

def action(parser): 
    action = \
        parser.add_parser(
            'template:mkca', 
            help='Make root certificate.'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/mkca.sh")