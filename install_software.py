import os
import subprocess
from logger import setup_logger

# Set up logger
log = setup_logger('InstallSoftware', '/var/log/arch_assistant.log')

def install_software(package_name):
    log.info(f"Installing {package_name}...")
    print(f"Installing {package_name}...")
    
    try:
        # Running pacman command with sudo to install the package
        subprocess.run(['sudo', 'pacman', '-S', package_name], check=True)
        print(f"{package_name} installed successfully!")
        log.info(f"{package_name} installed successfully!")
        
    except subprocess.CalledProcessError as e:
        error_message = f"Error installing {package_name}: {e}"
        print(error_message)
        log.error(error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        print(error_message)
        log.error(error_message)

# Example usage
# install_software('vim')