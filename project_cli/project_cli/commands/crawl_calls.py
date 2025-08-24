import os
import click
from project_cli.utils.get_services import get_services
from project_cli.utils.get_hosts import get_hosts
from project_cli.utils.get_history import get_history

@click.group(invoke_without_command=True)
@click.pass_context
def crawl_dir(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("No subcommand was invoked. Please use a subcommand.")
    

@crawl_dir.command()
def services(root_dir):
    if not os.path.exists(root_dir):
        print(f"❌ Directory does not exist: {root_dir}")
        return

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'query.txt':
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        query = f.read()
                    page = 1
                    page_size = 10
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
                    #
                except Exception as e:
                    print(f"⚠️ Error reading {file_path}: {e}")

def hosts(root_dir):
    if not os.path.exists(root_dir):
        print(f"❌ Directory does not exist: {root_dir}")
        return

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'query.txt':
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        query = f.read()
                    page = 1
                    page_size = 10
                    save_response = click.prompt("Do you want to save the response to a JSON file?", default=False, type=bool)

                    response = get_hosts(query, page=page, page_size=page_size, save_json=save_response)
                    total_records = response['total_records']

                    click.echo(f" {total_records} Results found for prompt. {int(total_records/ page_size)} Results Retrieved. ")
                    pages_json = response["page"]

                    while total_records > page_size*page:
                        if not click.prompt("Do you want to view the next page?", default="", show_default=False) == "":
                            break
                        else:
                            page += 1
                            response = get_hosts(query, page=page, page_size=page_size, save_json=save_response)
                            pages_json.extend(response["page"])
                            click.echo(f" {total_records} Results found for prompt. {int(total_records / (page_size*page))} Results Retrieved. ")
                    #
                except Exception as e:
                    print(f"⚠️ Error reading {file_path}: {e}")

# def histories(root_dir):