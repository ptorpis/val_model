# Financial Statements Exporter

## Overview
This script fetches and exports financial statements (Balance Sheet, Income Statement, and Cash Flow) for a given stock symbol. It retrieves data from Alpha Vantage and Yahoo Finance, processes it into structured Pandas DataFrames, and exports the results as a formatted Excel file. The exported statements are based on quarterly reporting. The date range can be anything from 1-15 years back. This is a refactored verion of my [financial_analysis](<https://github.com/ptorpis/financial_analysis>) project.

Please make sure to verify the validity and the accuracy of the data provided.

To use this script, you must obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

## Features
- Fetches financial statements from Alpha Vantage API.
- Retrieves company information (Name, Sector, Industry, Website) from Yahoo Finance.
- Processes financial statement data into readable Pandas DataFrames.
- Exports data into a well-formatted Excel file with multiple sheets.
- Validates stock ticker symbols before fetching data.

## Download and Installation
To download this project to your local machine, follow these steps:

### Download the ZIP File
1. Go to the [Releases](<https://github.com/ptorpis/val_model/releases>).
2. Select the latest release and download the ZIP file.
3. Extract the ZIP file to your desired location.

Then, navigate into the project directory:

```bash
cd your/repository_folder
```
## Quick Setup
To set up the program on you machine after downloading it, run:
```
python setup.py
```
This will set up your environment, download all the packages needed and promt you for your API key (if you don't have it at that moment, you can set it up later see also: [Configuration](##configuration))
## Manual Setup
### On Windows:
```
python -m venv .venv
```
To set up the environment (only needs to be done once), then whenever you want to use the program, run:
```
.venv\Scripts\activate
```
### On macOS/Linux:
```
python3 -m venv .venv
```
To set up the environment (only needs to be done once), then whenever you want to use the program, run:
```
source venv/bin/activate
```

### When you are done using the program:
```
deactivate
```
## Dependencies (manual setup only)
Ensure you have Python installed and install the required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
## Configuration
Once you have the key, go to the file `config/config.json` and paste your API key inside:
```json
{
    "api_key": "INSERT YOUR KEY HERE"
}
```
Do not share your key with others.

## Usage
Run the script with a stock ticker symbol:

```bash
python main.py AAPL
```
*Note: the program accepts both lower and upper case entries as the ticker, it runs a check to verify that the string provided is a ticker, but this check may not be 100% accurate, if you encounter issues with the program not accepting your ticker, feel free to reach out.*

### Optional Arguments
- **Specify Number of Years**: You can choose how many years of financial data to export (default is 5, max is 15).
  ```bash
  python main.py AAPL 10
  ```
This will export the quarterly statements for the last 10 years.

- **Skip Fetching New Data**: If you have already downloaded the data and just want to adjust the number of years in the Excel file, use the `--no-fetch` flag to avoid unnecessary API calls.
  ```bash
  python main.py AAPL 7 --no-fetch
  ```
This will export the quarterly statements for the last 7 years, and skip the API calls. (A free user has a maximum of 25 per day)

- **If you need help, use `-h` or `--help`**:
  ```bash
  python main.py --help
  ```

### Example Output Structure
An Excel file will be created in the `output/` directory, containing:
- **Cover Sheet** (Company Information)
- **Balance Sheet**
- **Income Statement**
- **Cash Flow Statement**

## Error Handling
- Checks for API key presence and validity.
- Detects and handles API rate limits.
- Checks for exising files when using `--no-fetch`.
- Ensures valid and existing stock tickers.
- Handles missing or malformed data.

## Disclaimer
- This project is for educational and informational purposes only.
- The data retrieved from Alpha Vantage and Yahoo Finance may be subject to limitations, inaccuracies, or delays.
- The author is not responsible for any financial losses or decisions made based on the data provided.
- Users should verify the accuracy of the data before moving forward.

## License
This project is licensed under the MIT License. You are free to modify and use it as needed.

## Contact

If you have any questions, suggestions, or otherwise, reach out at: ptorpis@gmail.com
