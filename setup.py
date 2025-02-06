import os
import subprocess
import sys
import json

VENV_DIR = ".venv"  # Your virtual environment directory
CONFIG_DIR = "config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def run_command(command):
    """Run a shell command and check for errors."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        sys.exit(1)


print("\nSetting up your Financial Statements Exporter environment...\n")

# Step 1: Create a virtual environment
run_command(f"{sys.executable} -m venv {VENV_DIR}")

# Step 2: Display activation command
if os.name == "nt":  # Windows
    activate_cmd = f"{VENV_DIR}\\Scripts\\activate"
else:  # macOS/Linux
    activate_cmd = f"source {VENV_DIR}/bin/activate"

print(f"Virtual environment created in `{VENV_DIR}`. To activate it, run:\n")
print(f"   {activate_cmd}\n")

# Step 3: Install dependencies
run_command(f"{sys.executable} -m pip install --upgrade pip")
run_command(f"{sys.executable} -m pip install -r requirements.txt")

print("Dependencies installed successfully.\n")

# Step 4: Ensure config directory exists and prompt for API key setup
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
    print("\nAPI key configuration file already exists.\n")

print("\nSetup complete! You can now activate your virtual environment and run the script.\n")
print(f"   To activate your environment, run: {activate_cmd}")
print("   Then you can run the program using:\n")
print("   python main.py AAPL\n")
print("Happy analyzing!\n")
