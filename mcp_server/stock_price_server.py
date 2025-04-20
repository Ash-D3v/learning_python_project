from mcp.server.fastmcp import FastMCP
import yfinance as yf

# Create an MCP server with a custom name
mcp = FastMCP("Stock Price Server")

@mcp.tool()
def get_stock_price(symbol: str) -> float:
    """
    Get the current stock price for a given symbol.
    
    Args:
        symbol (str): The stock symbol (e.g., 'AAPL' for Apple)
        
    Returns:
        float: The current stock price, or -1.0 if there's an error
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if not data.empty:
            price = data['Close'].iloc[-1]
            return float(price)
        else:
            info = ticker.info
            price = info.get("regularMarketPrice", None)
            if price is not None:
                return float(price)
            return -1.0
    except Exception:
        return -1.0
    
@mcp.resource('stock://{symbol}')
def stock_resource(symbol: str) -> str:
    """
    Resource endpoint to get stock price information.
    
    Args:
        symbol (str): The stock symbol
        
    Returns:
        str: Formatted string with the current price or error message
    """
    price = get_stock_price(symbol)
    if price < 0:
        return f"Error: Could not retrieve price for symbol '{symbol}'."
    return f"The current price of '{symbol}' is ${price:.2f}."

@mcp.tool()
def get_stock_history(symbol: str, period: str = '1mo') -> str:
    """
    Get historical stock data for a given symbol and time period.
    
    Args:
        symbol (str): The stock symbol
        period (str): Time period for historical data (default: '1mo')
        
    Returns:
        str: CSV formatted historical data or error message
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period)
        if data.empty:
            return f"No historical data found for symbol '{symbol}' with period '{period}'"
        csv_data = data.to_csv()
        return csv_data
    except Exception as e:
        return f"Error fetching historical data: {str(e)}"

@mcp.tool()
def compare_stocks(symbol1: str, symbol2: str) -> str:
    """
    Compare the current prices of two stocks.
    
    Args:
        symbol1 (str): First stock symbol
        symbol2 (str): Second stock symbol
        
    Returns:
        str: Comparison result or error message
    """
    price1 = get_stock_price(symbol1)
    price2 = get_stock_price(symbol2)
    if price1 < 0 or price2 < 0:
        return f"Error: Could not retrieve data for comparison of '{symbol1}' and '{symbol2}'."
    if price1 > price2:
        result = f"{symbol1} (${price1:.2f}) is higher than {symbol2} (${price2:.2f})."
    elif price1 < price2:
        result = f"{symbol1} (${price1:.2f}) is lower than {symbol2} (${price2:.2f})."
    else:
        result = f"Both {symbol1} and {symbol2} have the same price (${price1:.2f})."
    return result

if __name__ == "__main__":
    mcp.run()