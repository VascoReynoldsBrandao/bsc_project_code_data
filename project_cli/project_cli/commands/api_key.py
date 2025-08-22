import os
import click
from dotenv import set_key
from project_cli.config.settings import ENV_PATH, get_api_key
from project_cli.utils.key_validator import is_valid_modat_api_key

@click.command()
def check_key():
    """Check if API_KEY is set and valid."""
    api_key = get_api_key()
    if not api_key:
        click.echo("❌ API_KEY is not set.")
    elif is_valid_modat_api_key(api_key):
        click.echo("✅ API_KEY is set and valid.")
    else:
        click.echo("⚠️ API_KEY is set but invalid.")

@click.command()
def set_api_key():
    """Prompt user to set API_KEY and save to .env if valid."""
    api_key = click.prompt("Enter your API key", hide_input=True)

    if is_valid_modat_api_key(api_key):
        if not os.path.exists(ENV_PATH):
            with open(ENV_PATH, "w") as f:
                f.write("")
        set_key(ENV_PATH, "API_KEY", api_key)
        click.echo("✅ API_KEY saved to .env and is valid.")
    else:
        click.echo("❌ Invalid API_KEY. Please try again.")
