import sys

import click

from astro import sunsign

@click.command()
@click.argument('timestamp', default='', required=False)

def main(timestamp):
    if (timestamp == ''):
        timestamp = sys.stdin.read()
        
    try:
        timestamp = int(timestamp)
    except ValueError:
        click.echo("Invalid timestamp.")
        sys.exit(1)

    click.echo(sunsign(timestamp))
    sys.exit(0)
