import click
from project_cli.commands import greet
from project_cli.commands.api_key import check_key, set_api_key

@click.group()
def cli():
    """Project CLI Tool"""
    pass

cli.add_command(greet.greet)
cli.add_command(check_key)
cli.add_command(set_api_key)

if __name__ == "__main__":
    cli()