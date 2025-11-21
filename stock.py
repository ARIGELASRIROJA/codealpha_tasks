# 1. Hardcoded stock prices:
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 210,
    "INFY": 150,
    "AMZN": 300
}

portfolio = {}

# 2. Input stocks and quantity
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc) or 'done': ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    qty = input(f"Enter quantity for {stock}: ")
    if not qty.isdigit():
        print("Please enter a valid number.")
        continue
    qty = int(qty)
    portfolio[stock] = qty

# 3. Calculate total investment
total = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total += value
    print(f"- {stock}: {qty} shares x {stock_prices[stock]} = {value}")

print(f"Total Investment Value: {total}")

# 4. Optional: Save to file
save = input("Save to file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock}: {qty} shares x {stock_prices[stock]} = {value}\n")
        f.write(f"Total Investment Value: {total}\n")
    print("Saved to portfolio.txt")
