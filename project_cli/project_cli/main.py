import click
import traceback
from project_cli.commands import greet
from project_cli.commands.api_key import check_key, set_api_key
from project_cli.commands.manual_call import manual_call

@click.group()
def cli():
    """Project CLI Tool"""
    pass

cli.add_command(greet.greet)
cli.add_command(check_key)
cli.add_command(set_api_key)
cli.add_command(manual_call)

def main():
    try:
        cli()
    except Exception as e:
        click.echo(f"❌ Fatal error: {e}")
        click.echo(traceback.print_exc())

if __name__ == "__main__":
    main()