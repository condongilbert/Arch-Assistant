#!/bin/bash
BACKUP_DIR="/path/to/backup/dir"
echo "Backing up home directory..."
rsync -a --exclude='*.cache' /home/$USER $BACKUP_DIR
echo "Backup completed!"