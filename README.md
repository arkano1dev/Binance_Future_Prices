# Binance Futures Prices

This tool retrieves historical price data for multiple symbols from Binance using their API and saves them into separate CSV files. 

## Requirements

The following libraries are imported:

Binance's API

pandas

requests


## Installation 

1-Clone the repository

2-Install the required libraries mentioned in requirements.txt

3-Create a config.json file containing your Binance API key and secret key as follows:

*_{
    "API_KEY": "your_api_key_here",
    "SECRET_KEY": "your_secret_key_here"
}_*

4-Modify the symbols.csv file to include the symbols you want to retrieve historical data for

## Usage

The code imports the necessary libraries, including Binance's API, pandas, and requests. It then creates an instance of the Binance API client using the API key and secret key provided by the user in a config.json doc for making it secret and keep it private.

Next, the code retrieves the symbols from Binance using the client's exchangeInfo method and filtering the pairs of coins in trading status and the USDT currencies, which returns a list of dictionaries containing information about each symbol. The code then extracts the symbol names from the dictionaries and saves them into a CSV file using pandas' to_csv() method.

After the CSV file is created, the code reads it using pandas read_csv() method and loops through each symbol name. For each symbol, the code retrieves the historical price data using Binance's klines API endpoint, which returns a JSON object containing the open, high, low, and close prices, as well as other information, for each candlestick in the requested time period.

Then converts the JSON object into a pandas DataFrame and cleans it up by dropping unnecessary columns.

Finally, the DataFrame is saved into a CSV file using pandas' to_csv() method, with the filename being the symbol name appended with the date range of the historical data and the number os rows of the file.

## Output Data

After the analysis, an Excel file will be generated for each pair in the analyzed list, formatted accordingly.

![image](https://user-images.githubusercontent.com/62271657/233710490-4858cb08-ef4f-49fb-aa0f-b1f59c2a7d10.png)



