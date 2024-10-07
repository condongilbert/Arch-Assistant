import subprocess
import argparse

def update_system():
    subprocess.run(["sudo", "pacman", "-Syu"], check=True)

def install_package(package):
    subprocess.run(["sudo", "pacman", "-S", package], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arch Linux Assistant")
    parser.add_argument('--update', action='store_true', help='Update system')
    parser.add_argument('--install', type=str, help='Install a package')

    args = parser.parse_args()

    if args.update:
        update_system()
    if args.install:
        install_package(args.install)