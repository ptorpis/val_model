# Financial Statements Exporter

## Overview
This script fetches and exports financial statements (Balance Sheet, Income Statement, and Cash Flow) for a given stock symbol. It retrieves data from Alpha Vantage and Yahoo Finance, processes it into structured Pandas DataFrames, and exports the results as a formatted Excel file. The exported statements are based on quarterly reporting over the last 5 years. This is a refactored verion of my [financial_analysis](<https://github.com/ptorpis/financial_analysis>) project.

Please make sure to verify the validity and the accuracy of the data provided.

## Features
- Fetches financial statements from Alpha Vantage API.
- Retrieves company information (Name, Sector, Industry, Website) from Yahoo Finance.
- Processes financial statement data into readable Pandas DataFrames.
- Exports data into a well-formatted Excel file with multiple sheets.
- Validates stock ticker symbols before fetching data.

## Prerequisites
Ensure you have Python installed and install the required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
## Download and Installation
To download this project to your local machine, follow these steps:

### Option 1: Download the ZIP File
1. Go to the [Releases](<https://github.com/ptorpis/val_model/releases>).
3. Select **Download ZIP**.
4. Extract the ZIP file to your desired location.

Then, navigate into the project directory:

```bash
cd your/repository_folder
```

## Configuration
To use this script, you must obtain an API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key). Once you have the key, create a configuration file `config/config.json` and paste your API key inside:

```json
{
    "api_key": "INSERT YOUR KEY HERE"
}
```

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

- **If you need help, use -h or --help**:
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
