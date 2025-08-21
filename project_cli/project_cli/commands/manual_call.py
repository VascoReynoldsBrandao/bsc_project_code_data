import click
from project_cli.project_cli.utils import get_services, get_hosts, get_history


@click.group(invoke_without_command=True)
@click.pass_context
def manual_call(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("❌ Error: You must specify a subcommand.")
        click.echo("👉 Try one of: services, hosts, histories")
        ctx.exit(1)

@manual_call.command()
def services():
    query = click.prompt("Enter your search query for services")
    page = click.prompt("Enter page number", default=1, type=int)
    page_size = click.prompt("Enter page size", default=10, type=int)
    result = get_services(query, page=page, page_size=page_size)

@manual_call.command()
def hosts():
    query = click.prompt("Enter your search query for hosts")
    page = click.prompt("Enter page number", default=1, type=int)
    page_size = click.prompt("Enter page size", default=10, type=int)
    result = get_hosts(query, page=page, page_size=page_size)

@manual_call.command()
def histories():
    query = click.prompt("Enter your search query for histories")
    page = click.prompt("Enter page number", default=1, type=int)
    page_size = click.prompt("Enter page size", default=10, type=int)
    result = get_history(query, page=page, page_size=page_size)
