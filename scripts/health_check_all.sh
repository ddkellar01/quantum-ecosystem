#!/bin/bash
set -e

echo "Running health checks across all quantum ecosystem services..."

services=("http://localhost:8000/health" "http://localhost:5000/health")

for url in "${services[@]}"; do
    echo "Checking endpoint: ${url}"
    response=$(curl -s -o /dev/null -w "%{http_code}" ${url} || echo "000")
    if [ "${response}" -eq 200 ]; then
        echo "✅ ${url} is healthy."
    else
        echo "❌ ${url} returned status ${response}."
    fi
done
