# Financial Statements Exporter

## Overview
This script fetches and exports financial statements (Balance Sheet, Income Statement, and Cash Flow) for a given stock symbol. It retrieves data from Alpha Vantage and Yahoo Finance, processes it into structured Pandas DataFrames, and exports the results as a formatted Excel file. The exported statements are based on quarterly reporting over the last 5 years. This is a refactored verion of my [financial_analysis](<https://github.com/ptorpis/financial_analysis>) project

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
1. Go to the [GitHub repository](<https://github.com/ptorpis/val_model>).
2. Click on the **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file to your desired location.

### Option 2: Clone via Git (Alternative Method)
If you have Git installed, you can clone the repository using:

```bash
git clone https://github.com/ptorpis/val_model
```

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
python script.py AAPL
```
*Note: the program accepts both lower and upper case entries as the ticker, it runs a check to verify that the string provided is a ticker, but this check may not be 100% accurate, if you encounter issues with the program not accepting your ticker, feel free to reach out.*

### Example Output Structure
An Excel file will be created in the `output/` directory, containing:
- **Cover Sheet** (Company Information)
- **Balance Sheet**
- **Income Statement**
- **Cash Flow Statement**

## Code Breakdown
- `get_api_key(config_path)`: Retrieves API key from the config file.
- `get_statements(symbol)`: Fetches financial statements from Alpha Vantage.
- `get_info(ticker_symbol)`: Retrieves company info from Yahoo Finance.
- `process_statement(data_path)`: Parses JSON financial data into a DataFrame.
- `export(data_path, symbol)`: Formats and exports data to an Excel file.
- `validate_ticker(symbol)`: Checks if the ticker is valid using Yahoo Finance.
- `main(data_path, symbol)`: Coordinates the execution flow.

## Error Handling
- Checks for API key presence and validity.
- Detects and handles API rate limits.
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
