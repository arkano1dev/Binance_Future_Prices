Firstly, the code imports the necessary libraries, including Binance's API, pandas, and requests. It then creates an instance of the Binance API client using the API key and secret key provided by the user in a config.json doc for making it secret and keep it private.

Next, the code retrieves the symbols from Binance using the client's exchangeInfo method and filtering the pairs of coins in trading status and the USDT currencies, which returns a list of dictionaries containing information about each symbol. The code then extracts the symbol names from the dictionaries and saves them into a CSV file using pandas' to_csv() method.

After the CSV file is created, the code reads it using pandas read_csv() method and loops through each symbol name. For each symbol, the code retrieves the historical price data using Binance's klines API endpoint, which returns a JSON object containing the open, high, low, and close prices, as well as other information, for each candlestick in the requested time period.

The code then converts the JSON object into a pandas DataFrame and cleans it up by dropping unnecessary columns..

Finally, the DataFrame is saved into a CSV file using pandas' to_csv() method, with the filename being the symbol name appended with the date range of the historical data and the number os rows of the file.

Overall, this code provides a convenient way to retrieve historical price data for multiple symbols from Binance and save them into separate CSV files. It can be easily modified to retrieve data for a different exchange or time period, or to perform additional analysis on the data.



