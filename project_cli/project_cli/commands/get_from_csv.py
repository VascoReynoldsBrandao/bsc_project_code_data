import os
import click
import pandas as pd
from project_cli.utils.get_services import get_services
from project_cli.config.settings import DATA_DIR
from project_cli.utils.get_hosts import get_hosts
from project_cli.utils.get_history import get_history

@click.group(invoke_without_command=True)
@click.pass_context
# @click.option('--help', '-h', is_flag=True, help="Uses a csv with queries under a \'query\' column and retrieves the corresponding results storing them in a \'results\' and '\n_results\'.")
def get_from_csv(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("No subcommand was invoked. Please use a subcommand.")
    

@get_from_csv.command()
def services():
    file = click.prompt("Enter the path to the CSV file", type=str)
    if not os.path.exists(file):
        print(f"❌ File does not exist: {file}")
        return
    
    df = pd.read_csv(file)
    error_count = 0
    error_rows = []

    for index, row in df.iterrows():
        query = row['query']
        page = 1
        page_size = 100

        try: 
            response = get_services(query, page=page, page_size=page_size)
            total_records = response['total_records']
            click.echo(f" {total_records} Results found for prompt. {int(total_records/ page_size)} Results Retrieved. ")
            pages_json = response["page"]

            while total_records > page_size*page:
                if not click.prompt("Do you want to view the next page?", default="", show_default=False) == "":
                    break
                else:
                    page += 1
                    response = get_services(query, page=page, page_size=page_size)
                    pages_json.extend(response["page"])
                    click.echo(f" {total_records} Results found for prompt. {int(total_records / (page_size*page))} Results Retrieved. ")
            # row['results'] = pages_json
            # row['n_results'] = total_records
            df.at[index, 'results'] = str(pages_json)
            df.at[index, 'n_results'] = total_records
            print(f"✅ Finished processing query of row {index}")
        except Exception as e:
            error_count += 1
            error_rows.append(index)
            print(f"❌ Error processing query of row {index}: {e}")
    print(f"✅ Saving results to {file} with ❌{error_count} errors at rows {error_rows}")
    output_file = f"{DATA_DIR}/queries_services_output.csv"
    df.to_csv(output_file, index=False)

@get_from_csv.command()
def hosts():
    file = click.prompt("Enter the path to the CSV file", type=str)
    if not os.path.exists(file):
        print(f"❌ File does not exist: {file}")
        return

    df = pd.read_csv(file)
    error_count = 0
    error_rows = []

    for index, row in df.iterrows():
        query = row['query']
        page = 1
        page_size = 100

        try:
            response = get_hosts(query, page=page, page_size=page_size)
            total_records = response['total_records']
            click.echo(f" {total_records} Results found for prompt. {int(total_records/ page_size)} Results Retrieved. ")
            pages_json = response["page"]

            while total_records > page_size*page:
                if not click.prompt("Do you want to view the next page?", default="", show_default=False) == "":
                    break
                else:
                    page += 1
                    response = get_hosts(query, page=page, page_size=page_size)
                    pages_json.extend(response["page"])
                    click.echo(f" {total_records} Results found for prompt. {int(total_records / (page_size*page))} Results Retrieved. ")
            # row['results'] = pages_json
            # row['n_results'] = total_records
            df.at[index, 'results'] = pages_json
            df.at[index, 'n_results'] = total_records
            print(f"✅ Finished processing query of row {index}")
        except Exception as e:
            error_count += 1
            error_rows.append(index)
            print(f"❌ Error processing query on row {index}: {e}")
    print(f"✅ Saving results to {file} with ❌{error_count} errors at rows {error_rows}")
    output_file = f"{DATA_DIR}/queries_hosts_output.csv"
    df.to_csv(output_file, index=False)

@get_from_csv.command()
def histories():
    file = click.prompt("Enter the path to the CSV file", type=str)
    if not os.path.exists(file):
        print(f"❌ File does not exist: {file}")
        return

    df = pd.read_csv(file)
    error_count = 0
    error_rows = []

    for index, row in df.iterrows():
        since = row['since']
        port = row['port']
        transport = row['transport']
        ip = row['ip']
        try:
            response = get_history(since, ip, port, transport)
            print(f"✅ Finished processing query of row {index}")
            history_json = response["history"]
            # row['results'] = history_json
            # row['n_results'] = len(history_json)
            df.at[index, 'results'] = history_json
            df.at[index, 'n_results'] = len(history_json)
        except Exception as e:
            error_count += 1
            error_rows.append(index)
            print(f"❌ Error processing query on row {index}: {e}")
    print(f"✅ Saving results to {file} with ❌{error_count} errors at rows {error_rows}")
    output_file = f"{DATA_DIR}/history_queries.csv"
    df.to_csv(output_file, index=False)