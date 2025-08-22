import click
from project_cli.utils.get_services import get_services
from project_cli.utils.get_hosts import get_hosts
from project_cli.utils.get_history import get_history

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
    save_response = click.prompt("Do you want to save the response to a JSON file?", default=False, type=bool)
    
    response = get_services(query, page=page, page_size=page_size, save_json=save_response)
    total_records = response['total_records']
    click.echo(f" {total_records} Results found for prompt. {int(total_records/ page_size)} Results Retrieved. ")
    pages_json = response["page"]

    while total_records > page_size*page:
        if not click.prompt("Do you want to view the next page?", default="", show_default=False) == "":
            break
        else:
            page += 1
            response = get_services(query, page=page, page_size=page_size, save_json=save_response)
            pages_json.extend(response["page"])
            click.echo(f" {total_records} Results found for prompt. {int(total_records / (page_size*page))} Results Retrieved. ")

@manual_call.command()
def hosts():
    query = click.prompt("Enter your search query for hosts")
    page = click.prompt("Enter page number", default=1, type=int)
    page_size = click.prompt("Enter page size", default=10, type=int)
    save_response = click.prompt("Do you want to save the response to a JSON file?", default=False, type=bool)
    
    response = get_hosts(query, page=page, page_size=page_size, save_json=save_response)
    total_records = response['total_records']
    click.echo(f" {total_records} Results found for prompt. {int(total_records / page_size)} Results Retrieved. ")
    pages_json = response["page"]

    while total_records > (page_size*page):
        if not click.prompt("Do you want to view the next page?", default="", show_default=False) == "":
            break
        else:
            page += 1
            response = get_hosts(query, page=page, page_size=page_size, save_json=save_response)
            pages_json.extend(response["page"])
            click.echo(f" {total_records} Results found for prompt. {int(total_records / (page_size*page))} Results Retrieved. ")

@manual_call.command()
def histories():
    query = click.prompt("Enter your search query for histories")
    page = click.prompt("Enter page number", default=1, type=int)
    page_size = click.prompt("Enter page size", default=10, type=int)
    save_response = click.prompt("Do you want to save the response to a JSON file?", default=False, type=bool)
    
    response = get_history(query, page=page, page_size=page_size, save_json=save_response)
    total_records = response['total_records']
    click.echo(f" {total_records} Results found for prompt. {int(total_records / page_size)} Results Retrieved. ")
    pages_json = response["page"]

    while total_records > (page_size*page):
        if not click.prompt("Do you want to view the next page?", default="", show_default=False) == "":
            break
        else:
            page += 1
            response = get_history(query, page=page, page_size=page_size, save_json=save_response)
            pages_json.extend(response["page"])
            click.echo(f" {total_records} Results found for prompt. {int(total_records / (page_size*page))} Results Retrieved. ")
