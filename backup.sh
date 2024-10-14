#!/bin/bash

# Set variables
BACKUP_DIR="/path/to/backup/dir/backup_$(date +'%Y-%m-%d_%H-%M-%S')"
LOG_FILE="/var/log/arch_assistant.log"

# Logging function
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - BackupScript - $1" >> "$LOG_FILE"
}

# Start the backup process
log_message "Starting backup of home directory..."
echo "Backing up home directory to $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"

# Perform the backup, excluding cache files
rsync -a --exclude='*.cache' /home/$USER "$BACKUP_DIR" >> "$LOG_FILE" 2>&1

# Check if the rsync command succeeded
if [ $? -eq 0 ]; then
    log_message "Backup completed successfully!"
    echo "Backup completed!"
else
    log_message "Backup failed!"
    echo "Backup failed! Check $LOG_FILE for details."
fi