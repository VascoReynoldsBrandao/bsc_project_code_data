import click
import traceback
from project_cli.commands import greet
from project_cli.commands.api_key import check_key, set_api_key
from project_cli.commands.manual_call import manual_call
from project_cli.commands.get_from_csv import get_from_csv
from project_cli.commands.extract_from_csv import extract_from_csv
from project_cli.commands.generate_history_queries import generate_history_queries


@click.group()
def cli():
    """Project CLI Tool"""
    pass

cli.add_command(greet.greet)
cli.add_command(check_key)
cli.add_command(set_api_key)
cli.add_command(manual_call)
cli.add_command(get_from_csv)
cli.add_command(extract_from_csv)
cli.add_command(generate_history_queries)

def main():
    try:
        cli()
    except Exception as e:
        click.echo(f"❌ Fatal error: {e}")
        click.echo(traceback.print_exc())

if __name__ == "__main__":
    main()