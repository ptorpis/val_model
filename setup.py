import os
import subprocess
import sys
import json

CONFIG_DIR = "config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def run_command(command):
    """Run a shell command and check for errors."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        sys.exit(1)


print("\nSetting up your Financial Statements Exporter environment...\n")

# Step 1: Install dependencies globally or in the existing environment
print("Installing required dependencies...\n")
run_command(f"{sys.executable} -m pip install --upgrade pip")
run_command(f"{sys.executable} -m pip install -r requirements.txt")

print("Dependencies installed successfully.\n")

# Step 2: Ensure config directory exists and prompt for API key setup
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

if not os.path.exists(CONFIG_FILE):
    print("\nYou need to configure your API key for Alpha Vantage.")
    api_key = input("Enter your Alpha Vantage API Key (or press Enter to set it later): ").strip()

    config_data = {"api_key": api_key} if api_key else {"api_key": "INSERT YOUR KEY HERE"}

    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=4)

    print(f"API key configuration file created at `{CONFIG_FILE}`.")
else:
    print("API key configuration file already exists.\n")

print("Setup complete! You can now run the program using:\n")
print("   python main.py AAPL\n")
print("Happy analyzing!\n")
