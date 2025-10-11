import argparse 
import sys 

# Create root parser. 
parser = argparse.ArgumentParser(
    prog="DKHFST CLI Utility",
    description="Utility CLI tool for DKHFST."
)

subparsers = parser.add_subparsers(
    title="subcommands",
    description="valid subcommands",
    help="additional help",
    dest="command"
)

# -------------
# Load commands
# -------------

# --- Context for 'dkhfst'.
import cli.contexts.template.context as TemplateContext
TemplateContext.create(subparsers)


# Run command.
args = parser.parse_args()

if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()

