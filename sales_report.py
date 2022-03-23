"""Generate sales report showing total melons each salesperson sold."""
'''Anna Parker|1881.91|13
name|total amount for order|total melons sold'''

sales_records = {}

f = open('sales-report.txt')
##iterates through the file line by line (\n to \n)
for line in f:
    line = line.rstrip()##clears the \nbreaks
    entries = line.split('|')##creates a list for each item in line
    salesperson = entries[0]##establishes variable for saleperson name
    melons = int(entries[2])##establishes variable for total melons sold

    sales_records[salesperson] = sales_records.get(salesperson, 0) + melons


for sale in sorted(sales_records):
    print(f"{sale} sold {sales_records[sale]} melons.")