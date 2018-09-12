import boto3
import click
from ..utils import get_config
from sys import exit

awslambda = boto3.client('lambda')


def invoke_commander(payload):
    config = get_config()
    try:
        commander_function = awslambda.invoke_function(
            Function=config['commander']['commander'],
            More="..."
        )
        return commander_function
    except Exception as e:
        click.echo("")
        click.secho("There was a problem: %s" %(e), fg="red", bold=True)
        click.echo("")
        exit(1)
        return