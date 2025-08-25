import pandas as pd
import json
import ast
from project_cli.utils.extract_info import extract_services, extract_hosts, extract_history

def extract_services_responses(file):
    df = pd.read_csv(file)

    final_df = pd.DataFrame()

    for index, row in df.iterrows():
        results = row['results']
        # Try to parse as JSON, fallback to ast.literal_eval if it fails
        try:
            results_json = json.loads(results)
        except json.JSONDecodeError:
            try:
                results_json = ast.literal_eval(results)
            except Exception:
                continue  # skip rows with invalid results
        results_df = extract_services(results_json)
        final_df = pd.concat([final_df, results_df], ignore_index=True)

    return final_df

def extract_hosts_responses(file):
    df = pd.read_csv(file)

    final_df = pd.DataFrame()

    for index, row in df.iterrows():
        results = row['results']
        results_json = json.loads(results)
        results_df = extract_hosts(results_json)
        final_df = pd.concat([final_df, results_df], ignore_index=True)

    return final_df

def extract_history_responses(file):
    df = pd.read_csv(file)

    final_df = pd.DataFrame()

    for index, row in df.iterrows():
        results = row['history']
        results_json = json.loads(results)
        results_df = extract_history(results_json)
        final_df = pd.concat([final_df, results_df], ignore_index=True)

    return final_df
