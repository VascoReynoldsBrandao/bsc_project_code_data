import click
import os
from project_cli.utils.extract_responses import extract_services_responses
from project_cli.config.settings import DATA_DIR

@click.group(invoke_without_command=True)
@click.pass_context
# @click.option('--help', '-h', is_flag=True, help="Given a csv ouput from the get-from-csv command, makes a csv only with MODAT Magnify result information.")
def extract_from_csv(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("No subcommand was invoked. Please use a subcommand.")

@extract_from_csv.command()
def services():
    file = click.prompt("Enter the path to the CSV file", type=str)
    if not os.path.exists(file):
        print(f"❌ File does not exist: {file}")
        return
    """Extract services from a CSV file."""
    df = extract_services_responses(file)

    df.to_csv(f"{DATA_DIR}/extracted_service_data.csv", index=False)
    click.echo("✅ Services extracted successfully.")

