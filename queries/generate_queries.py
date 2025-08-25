import pandas as pd

# Load the datasets
df_gpt = pd.read_csv('target_ips_unique_gpt.csv')
df_dps = pd.read_csv('target_ips_unique_dpk.csv')

# Combine the datasets
df = pd.concat([df_gpt, df_dps])

# Check total number of rows
len(df)

# Construct query string for each IP
df['query'] = "ip=" + df['ip'] + " and " + "(service=siemens or service=telnet or service=modbus or service=ftp or service=dnp3)"

# Placeholder columns for results
df['n_results'] = "..."
df['results'] = "..."

# Save to CSV
df.to_csv('queries.csv', index=False)
df['query'] = "ip=" + df['ip'] + " and service=http"
df.to_csv('http_queries.csv', index=False)
