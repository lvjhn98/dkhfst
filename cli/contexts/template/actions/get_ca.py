import os 

def action(parser): 
    action = \
        parser.add_parser(
            'template:get-ca', 
            help='Get root certificate from Caddy.'
        )
    action.set_defaults(func=handle)

def handle(args):
    os.system("bash ./scripts/template/get-ca.sh")