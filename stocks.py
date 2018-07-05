stock_dict = { "GM": "General Motors", "MSFT": "Microsoft", "AMD": "Advanced Micro Devices", "APPL": "Apple", "INTC": "Intel Corporation"}
purchases = [("GM", 100, "20-jun-2018", 52), ("MSFT", 24, "16-mar-2018", 98), ("INTC", 75, "23-jan-2018", 115), ("GM", 50, "13-jan-2018", 47)]

def report(list=purchases, stocks=stock_dict):
	value_report = []
	for stock in list:
		name = stocks[stock[0]]
		value = "$" + str(stock[1] * stock[3])
		value_report.append({name, value})
	return value_report

def report_by_ticker(list=purchases, stocks=stock_dict):
	tickers = {}
	for stock in list:
		name = stocks[stock[0]]
		value = stock[1]
		if name in tickers.keys():
			value += tickers[name]
			print(value)
		tickers.update({name: value})
	return tickers

print(report())
print(report_by_ticker())