# Stock Price Server

A Python-based server that provides real-time stock price information and historical data using the Yahoo Finance API.

> **Note**: This project was inspired by the tutorial [Building a Simple MCP Server](https://www.kdnuggets.com/building-a-simple-mcp-server) from KDnuggets.

## Features

- Get current stock prices for any symbol
- Retrieve historical stock data
- Compare prices between two stocks
- RESTful API endpoints for easy integration

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ashutoshdas-dev/learning_python_project.git
cd learning_python_project/mcp_server
```

2. Create and activate a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate
```

3. Install required packages:
```bash
pip install mcp-server
pip install yfinance
pip install fastapi
pip install uvicorn
```

## Usage

1. Start the server:
```bash
mcp dev stock_price_server.py
```

2. The server provides the following endpoints:

- Get current stock price:
  ```
  GET stock://{symbol}
  ```
  Example: `stock://AAPL` returns the current Apple stock price

3. Available tools:

- `get_stock_price(symbol)`: Returns the current price of a stock
- `get_stock_history(symbol, period='1mo')`: Returns historical data in CSV format
- `compare_stocks(symbol1, symbol2)`: Compares prices of two stocks

## Example Usage

```python
# Get current price
price = get_stock_price("AAPL")
print(f"Apple stock price: ${price:.2f}")

# Get historical data
history = get_stock_history("GOOGL", period="1y")
print(history)

# Compare stocks
comparison = compare_stocks("MSFT", "AMZN")
print(comparison)
```

## Error Handling

- The server returns -1.0 for invalid symbols or when data cannot be retrieved
- Error messages are provided in a user-friendly format
- All API calls include proper exception handling

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Original tutorial: [Building a Simple MCP Server](https://www.kdnuggets.com/building-a-simple-mcp-server) 



