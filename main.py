import requests
import json
import yfinance as yf
import pandas as pd
import re
import openpyxl
from datetime import datetime
import os
import argparse

CONFIG_PATH = 'config/config.json'
DATA_PATH = 'data'

sheets = [
    'BALANCE_SHEET',
    'INCOME_STATEMENT',
    'CASH_FLOW'
]

def get_api_key(config_path):
    """Retrieves the API key from a configuration file."""
    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
            api_key = config_data.get('api_key')
            if not api_key:
                raise ValueError("API key not found in configuration file.")
            return api_key
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error reading API key: {e}")

def get_statements(symbol):
    """Fetches financial statements for a given stock symbol and saves them as JSON files."""
    try:
        api_key = get_api_key(CONFIG_PATH)
    except RuntimeError as e:
        print(e)
        return

    if api_key == 'INSERT YOUR KEY HERE':
        print("Please provide an API key. (config/config.json)")
        return

    for sheet in sheets:
        url = f'https://www.alphavantage.co/query?function={sheet}&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()

        # Check for API rate limit message
        if "Information" in data:
            print(f"API Limit Reached: {data['Information']}")
            return -1 # Stop execution if rate limit is reached
        
        # Ensure output directory exists
        os.makedirs(DATA_PATH, exist_ok=True)

        # Save the response data to a JSON file
        file_path = os.path.join(DATA_PATH, f"{symbol}_{sheet}.json")
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Saved: {file_path}")  # Logging success
        
    return 0


def get_info(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        company_name = ticker.info.get("longName", "Unknown Company Name")
        sector = ticker.info.get("sector", "Unknown Sector")
        industry = ticker.info.get("industry", "Unknown Industry")
        website = ticker.info.get("website", "N/A")

        return {
            "company_name": company_name,
            "sector": sector,
            "industry": industry,
            "website": website
        }
        
    except:
        print("Unable to fetch company data.")
        return {
            "company_name": "Unknown Company Name",
            "sector": "Unknown Sector",
            "industry": "Unknown Industry",
            "website": "N/A"
            }


def process_statement(data_path):
    with open(data_path, 'r') as file:
        data = json.load(file)
    quarterly = data["quarterlyReports"]


    periods = []
    for i in range(20):
        periods.append(quarterly[i]["fiscalDateEnding"])

    if quarterly:
        keys_list = list(quarterly[0].keys())
    
    title_case_keys = []
    for i in range(len(keys_list)):
        current = re.sub(r'([a-z])([A-Z])', r'\1 \2', keys_list[i])
        title_case_keys.append(current.title()) 

    statement = {}
    statement["Keys"] = title_case_keys[2:] # exclude fiscalDateEnding and reportedCurrency to match the length of the other lists below
    for period in range(len(periods)):
        values = []
        for key in range(2, len(keys_list)): # from 2 to only get the numbers
            if quarterly[period][keys_list[key]] != 'None':
                values.append(quarterly[period][keys_list[key]])
            else:
                values.append(0)
        statement[quarterly[period][keys_list[0]]] = values

    df = pd.DataFrame(statement)
    return df


def export(data_path, symbol):
    # Retrieve company information
    company_info = get_info(symbol)

    # Create the cover sheet as a DataFrame
    cover_data = {
        "Company Name": [company_info['company_name']],
        "Sector": [company_info['sector']],
        "Industry": [company_info['industry']],
        "Website": [company_info['website']],
        "Retrieved": [datetime.now()]
    }
    cover_df = pd.DataFrame(cover_data)

    # Process other statements
    balance_sheet = process_statement(f'{data_path}/{symbol}_{sheets[0]}.json')
    income_statement = process_statement(f'{data_path}/{symbol}_{sheets[1]}.json')
    cash_flow = process_statement(f'{data_path}/{symbol}_{sheets[2]}.json')

    with pd.ExcelWriter(f'output/{symbol}_statements.xlsx', engine='openpyxl') as writer:
        
        # Write the cover sheet first
        cover_df.to_excel(writer, sheet_name="Cover Sheet", index=False)
        
        balance_sheet.iloc[:, 1:] = balance_sheet.iloc[:, 1:].apply(pd.to_numeric)
        income_statement.iloc[:, 1:] = income_statement.iloc[:, 1:].apply(pd.to_numeric)
        cash_flow.iloc[:, 1:] = cash_flow.iloc[:, 1:].apply(pd.to_numeric)

        balance_sheet.to_excel(writer, sheet_name='Balance Sheet', index=False)
        income_statement.to_excel(writer, sheet_name='Income Statement', index=False)
        cash_flow.to_excel(writer, sheet_name='Cash Flow', index=False)
        
        workbook = writer.book
        
        custom_format = '0,,;(0,,)'
        short_date_format = 'MM/DD/YYYY'

        # Loop through each sheet and apply formatting
        for sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
            
            # Apply custom format to each cell in the sheet (excluding headers)
            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
                for cell in row:
                    cell.number_format = custom_format
            
            if sheet_name == "Cover Sheet":
                retrieved_cell = sheet.cell(row=2, column=5)
                retrieved_cell.number_format = short_date_format  # Apply the date format

                for col_num, column in enumerate(sheet.columns, 1):
                    column_letter = openpyxl.utils.get_column_letter(col_num)  # Convert column number to letter
                    sheet.column_dimensions[column_letter].width = 25
            
            # Set column width for all columns except the first one (14 pixels)
            if sheet_name != "Cover Sheet":
                for col_num, column in enumerate(sheet.columns, 1):
                    if col_num != 1:  # Skip the first column
                        column_letter = openpyxl.utils.get_column_letter(col_num)
                        sheet.column_dimensions[column_letter].width = 13


def validate_ticker(symbol):
    """Validates and checks if the ticker exists using Yahoo Finance."""
    symbol = symbol.strip().upper()
    if not re.match(r"^[A-Z0-9]{1,5}$", symbol):
        raise argparse.ArgumentTypeError(f"Invalid ticker: '{symbol}'. Must be 1-5 letters/numbers.")

    # Check if the ticker exists
    if not yf.Ticker(symbol).history(period="1d").empty:
        return symbol
    else:
        raise argparse.ArgumentTypeError(f"Ticker '{symbol}' not found in Yahoo Finance.")

    

def main(data_path, symbol):
    gs = get_statements(symbol)
    if gs != 0:
        return
    export(data_path, symbol)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Financial Statements for a given Company")
    parser.add_argument('symbol', type=validate_ticker, help="The company's ticker (e.g. AAPL, MSFT)")

    args = parser.parse_args()    
    main(DATA_PATH, args.symbol)