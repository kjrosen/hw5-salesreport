"""Generate sales report showing total melons each salesperson sold."""
'''Anna Parker|1881.91|13
name|total amount for order|total melons sold'''

##corresponding lists of salespeople and their total melons sold. can be a dict
salespeople = []
melons_sold = []

f = open('sales-report.txt')
##iterates through the file line by line (\n to \n)
for line in f:
    line = line.rstrip()##clears the \nbreaks
    entries = line.split('|')##creates a list for each item in line
    salesperson = entries[0]##establishes variable for saleperson name
    melons = int(entries[2])##establishes variable for total melons sold

    '''this can be handled by adding names as keys and melons sold as values'''
    if salesperson in salespeople:##if the name is in our salesperson list
        position = salespeople.index(salesperson)##establishes their index
        melons_sold[position] += melons##adds total melons sold to their larger sales record      
    else:
        salespeople.append(salesperson)##if not already in the list, add them
        melons_sold.append(melons)##and add their melon sales

##prints the total sales per person
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')