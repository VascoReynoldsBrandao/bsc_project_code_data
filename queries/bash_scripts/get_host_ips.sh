#!/bin/bash

# Paste your access token here
ACCESS_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl9pZCI6IjY4MmUyNzYxLWNlY2ItNDY0ZS05NWQxLTIxOTIyNjdhMzZmNyIsInVzZXJfaWQiOiJhM2Y0MTg3Mi1lMDYxLTcwYzktOTRmMi00MzZlYTU5ZjExNDYiLCJleHAiOjE3NTYzMzkyMDAsImlhdCI6MTc1NTgwNTMxN30.KjA4LuEcIYfByuTOa0quR1LTQNIJ7Ur3gZTJPnsNiDE"

QUERY_FILE="query.txt"
OUTPUT_FILE="ip_results.txt"
> "$OUTPUT_FILE"

while IFS= read -r query || [ -n "$query" ]; do
    # Skip empty lines
    if [ -z "$query" ]; then
        continue
    fi

    page=1
    page_size=100
    total_pages=1

    while [ "$page" -le "$total_pages" ]; do
        # Safely encode query
        encoded_query=$(jq -Rs <<< "$query")

        # Make POST request
        response=$(curl -s -X POST "https://api.magnify.modat.io/host/search/v1" \
            -H "Accept: application/json" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $ACCESS_TOKEN" \
            -d "{\"query\": $encoded_query, \"page\": $page, \"page_size\": $page_size}")

        # Extract total_pages
        if [ "$page" -eq 1 ]; then
            total_pages=$(echo "$response" | jq '.total_pages')
            if [ "$total_pages" -eq 0 ]; then
                echo "⚠️ No results for query: $query"
                break
            fi
        fi

        # Extract IPs
        echo "$response" | jq -r '.page[] | select(.ip != null) | .ip' >> "$OUTPUT_FILE"

        page=$((page + 1))
        sleep 1
    done
done < "$QUERY_FILE"

echo "✅ Done. IPs saved to $OUTPUT_FILE"
