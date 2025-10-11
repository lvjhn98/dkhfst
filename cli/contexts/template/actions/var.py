import os 

def action(parser): 
    action = \
        parser.add_parser('template:var', help='Greet someone')
    action.add_argument(
        'key', type=str, help='Variable to display.'
    )
    action.set_defaults(func=handle)


def handle(args):
    print(os.environ.get(args.key))