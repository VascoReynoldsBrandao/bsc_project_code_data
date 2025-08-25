import click
import os
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from project_cli.config.settings import DATA_DIR

@click.command()
# @click.option('--help', '-h', is_flag=True, help="Uses csv of service search responses and makes lists of queries for histories.")
def generate_history_commands():
    file = click.prompt("Enter the path to the CSV file", type=str)
    if not os.path.exists(file):
        print(f"❌ File does not exist: {file}")
        return

    df = pd.read_csv(file)
    
    since = datetime.today() - relativedelta(months=1) + timedelta(days=1)
    since = since.strftime('%Y-%m-%dT%H:%M:%SZ')

    rows = []
    for index, row in df.iterrows():
        ip = row['ip']
        port = row['service_port']
        transport = row['service_transport']
        rows.append({
            'ip': ip,
            'port': port,
            'transport': transport,
            'since': since,
            'n_results': "...",
            'results': "..."
        })

    df_2 = pd.DataFrame(rows, columns=['ip', 'port', 'transport', 'since', 'n_results', 'results'])

    output_file = f"{DATA_DIR}/history_queries.csv"
    df_2.to_csv(output_file, index=False)

    click.echo(f"✅ History commands generated successfully: {output_file}")
