import sys
from datetime import date

import click

from zodiac import sunsign12, sunsign13

@click.command()
@click.option('--with-ophiuchus', '-o', is_flag=True, help='Include Ophiuchus as a sign (deprecated).')
@click.argument('timestamp', default='', required=False)

def main(timestamp, with_ophiuchus):
    if (timestamp == ''):
        timestamp = sys.stdin.read()
        
    try:
        timestamp = int(timestamp)
    except ValueError:
        click.echo("Invalid timestamp.")
        sys.exit(1)

    birthdate = date.fromtimestamp(timestamp)
    if (with_ophiuchus):
        sign = sunsign13(birthdate)
    else:
        sign = sunsign12(birthdate)

    click.echo(sign)
    sys.exit(0)
