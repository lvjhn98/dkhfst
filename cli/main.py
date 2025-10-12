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

# --- Context for 'template'.
import cli.contexts.template.context as TemplateContext
TemplateContext.create(subparsers)

# --- Context for 'compose'.
import cli.contexts.compose.context as ComposeContext
ComposeContext.create(subparsers)

# Run command.
args = parser.parse_args()

if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()

