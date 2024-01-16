PURCHASED_STOCKS = 2000
PRICE_PER_STOCKS  = 40.00
BROKER_COMMISSION = 0.03
total_stock_price = PRICE_PER_STOCKS*PURCHASED_STOCKS
cost_of_broker = total_stock_price*BROKER_COMMISSION
sold_stocks = PURCHASED_STOCKS*42.75
broker = sold_stocks*BROKER_COMMISSION
print(f"Joe paid ${total_stock_price:.2f} for the stock. ")
print(f"Joe paid his broker ${cost_of_broker:.2f} when he bought the stock.")
print(f"Joe sold the stock for ${sold_stocks:.2f}.")
print(f"Joe paid his broker ${broker:.2f} after he sold the stock.")
print(f"joe had ${sold_stocks-broker-cost_of_broker-total_stock_price:.2f} left.")