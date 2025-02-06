import os
import subprocess
import sys
import json

VENV_DIR = ".venv"  # Virtual environment directory
CONFIG_DIR = "config"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def run_command(command):
    """Run a shell command and check for errors."""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        sys.exit(1)


print("\nSetting up your Financial Statements Exporter environment...\n")

# Step 1: Create the virtual environment
run_command(f"{sys.executable} -m venv {VENV_DIR}")

# Step 2: Determine the correct pip path inside the virtual environment
if os.name == "nt":  # Windows
    pip_path = os.path.join(VENV_DIR, "Scripts", "python.exe") + " -m pip"
    activate_cmd = f"{VENV_DIR}\\Scripts\\activate"
else:  # macOS/Linux
    pip_path = os.path.join(VENV_DIR, "bin", "python") + " -m pip"
    activate_cmd = f"source {VENV_DIR}/bin/activate"

print(f"Virtual environment created in `{VENV_DIR}`.\n")
print(f"   To activate it, run:\n   {activate_cmd}\n")

# Step 3: Install dependencies inside the virtual environment
run_command(f"{pip_path} install --upgrade pip")
run_command(f"{pip_path} install -r requirements.txt")

print("Dependencies installed successfully inside the virtual environment.\n")

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
    print("API key configuration file already exists.\n")

print("Setup complete! You can now activate your virtual environment and run the script.\n")
print(f"   To activate your environment, run:\n   {activate_cmd}")
print("   Then run the program using:\n   python main.py AAPL\n")
print("Happy analyzing!\n")