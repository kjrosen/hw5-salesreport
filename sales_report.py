import sys

"""Generate sales report showing total melons each salesperson sold."""
'''Anna Parker|1881.91|13
name|total amount for order|total melons sold'''

def format_report(file = sys.argv[1]):
    '''opens and formats the file into a dictionary
    
    keys are the salesperson names, value is the total melons sold'''

    sales_records = {}

    with open(file) as report:
        for line in report:
            line = line.rstrip()
            record = line.split("|")

            name, cost, melons = record
            melons = int(melons)
            cost = float(melons)

            sales_records[name] = sales_records.get(name, 0) + melons

    report.close()
    return sales_records


def print_report(sales_record):
    '''prints out a report of how many melons each sales person sold
    
    takes in a dictionary with keys as names and values as melons sold'''

    for salesperson, melons_sold in sorted(sales_record.items()):
        print(f"{salesperson} sold {melons_sold} melons.")


print_report(format_report())