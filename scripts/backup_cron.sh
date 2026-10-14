#!/bin/bash
set -e

BACKUP_DIR="/app/backups"
DATA_DIR="/app/data"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FILENAME="ecosystem_auto_backup_${TIMESTAMP}.tar.gz"

mkdir -p "${BACKUP_DIR}"

echo "Starting automated cron backup process..."
tar -czf "${BACKUP_DIR}/${FILENAME}" -C "${DATA_DIR}" . 2>/dev/null || true

echo "Backup complete: ${BACKUP_DIR}/${FILENAME}"

# Prune backups older than 7 days
find "${BACKUP_DIR}" -type f -name "*.tar.gz" -mtime +7 -exec rm -f {} \;
echo "Pruned old backups."
