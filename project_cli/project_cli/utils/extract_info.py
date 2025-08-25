import pandas as pd
from project_cli.config.settings import get_host_cols, get_service_cols

def format_host_services(df):
    df['services'] = df['services'].apply(
        lambda services_list: [
            f"{service['transport']}/{service['port']}/{service['protocol']}/{service['scanned_at']}" 
            for service in services_list
        ] if services_list else []
    )
    return df

def extract_services(response_pages):
    pages = response_pages
    df = pd.json_normalize(pages, sep='_')
    df = df.apply(lambda col: col.map(lambda x: x if not isinstance(x, list) else ', '.join(map(str, x))))
    
    dt_cols = ['service_tls_valid_from', 'service_tls_expires_at', 'service_scannet_at']
    for col in dt_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    df = df.where(pd.notnull(df), None)
    df = df.replace('', None)

    df = df.reindex(columns=get_service_cols(), fill_value=None)
    
    return df

def extract_hosts(response_pages):
    pages = response_pages
    df = pd.json_normalize(pages, sep='_')
    df = format_host_services(df)
    df = df.apply(lambda col: col.map(lambda x: x if not isinstance(x, list) else ', '.join(map(str, x))))
    
    dt_cols = ['service_tls_valid_from', 'service_tls_expires_at', 'service_scannet_at']
    for col in dt_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    df = df.where(pd.notnull(df), None)
    df = df.replace('', None)

    df = df.reindex(columns=get_host_cols(), fill_value=None)

    return df

def extract_history(response):
    history = response["history"]
    df = pd.json_normalize(history, sep='_')
    df = format_host_services(df)
    df = df.apply(lambda col: col.map(lambda x: x if not isinstance(x, list) else ', '.join(map(str, x))))
    
    dt_cols = ['service_tls_valid_from', 'service_tls_expires_at', 'service_scannet_at']
    for col in dt_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    df = df.where(pd.notnull(df), None)
    df = df.replace('', None)

    return df
