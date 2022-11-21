#items = int(input('How many items do you have today? '))
#print(items)

#for i in range(items):
    #i = str(input('Please put in the first product name: '))


product1_name, product1_price = input('Please put in the first product name: '), float(input('Put in the price: '))
product2_name, product2_price = input('Please put in the second product name: '), float(input('Put in the price: '))
product3_name, product3_price = 'Monitor', 156.45

company_name = 'Gabriel Woods Company'
company_address = '410 Washington Street'
company_city = 'Blacksburg, Virginia'

message = 'Thanks for shopping with us today'

#Creating a top border
print('*' * 50)
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_city.title()))
print('\t\t{}'.format(company_address.title()))
#Print a line between sections
print('=' * 50)

print('\tProduct Name\tProduct Price')
#Create a print statement for each item
print('\t{}\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))
print('=' * 50)

#Print header section of total
print('\t\t\tTotal')
total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))
print('=' * 50)