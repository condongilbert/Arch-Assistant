import os
import subprocess

def install_software(package_name):
    print(f"Installing {package_name}...")
    try:
        subprocess.run(['sudo', 'pacman', '-S', package_name], check=True)
        print(f"{package_name} installed successfully!")
    except subprocess.CalledProcessError:
        print(f"Error installing {package_name}.")