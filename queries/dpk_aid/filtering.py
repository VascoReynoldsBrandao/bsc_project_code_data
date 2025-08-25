import pandas as pd

# Load the dataset
df = pd.read_csv('deepseek_queries_relevant_check_windfarms.csv')

# Filter by protocol and distance
siemens = df[(df['protocol'] == "siemens") & (df['distance'] < 50)]
modbus  = df[(df['protocol'] == "modbus") & (df['distance'] < 100)]
ftp     = df[(df['protocol'] == "ftp") & (df['distance'] < 50)]

# Combine filtered slices into one DataFrame
df_2 = pd.concat([siemens, modbus, ftp]).drop_duplicates().reset_index(drop=True)

# Save combined DataFrame to CSV
df_2.to_csv('chosen_queries_windfarms.csv', index=False)

# Extract IP and protocol columns, remove duplicates
df_3 = df_2[['ip', 'protocol']].drop_duplicates()

# Sort by IP address
df_3 = df_3.sort_values(by='ip')

# Save final list of target IPs
df_3.to_csv('target_ips.csv', index=False)

df_4 = (
    df_2.groupby('ip')['protocol']
    .apply(lambda x: sorted(set(x)))  # Optional: sort the list
    .reset_index()
    .rename(columns={'protocol': 'protocols'})
)
df_4.to_csv('target_ips_unique.csv', index=False)
