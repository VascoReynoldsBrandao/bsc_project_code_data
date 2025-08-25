#!/bin/bash

# Input file with IPs (one per line)
input_file="ips.txt"

# Output file
output_file="ipinfo_output.txt"

# Start JSON array
echo "[" > "$output_file"

# Counter to track last line
count=0
total=$(wc -l < "$input_file")

# Loop through IPs
while IFS= read -r ip; do
    echo "Fetching $ip..."
    curl -s "https://ipinfo.io/$ip/json" >> "$output_file"
    count=$((count + 1))
    if [ "$count" -lt "$total" ]; then
        echo "," >> "$output_file"
    fi
done < "$input_file"

# Close JSON array
echo "]" >> "$output_file"

echo "✅ Done. Output saved to $output_file"

