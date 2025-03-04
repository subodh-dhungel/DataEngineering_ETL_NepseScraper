stock_price = [290,295,312,300,320]
print(stock_price)

#insert an object to the specified index
stock_price.insert(5,350)
print(stock_price)

#remove the first occurance of a value
stock_price.remove(295)
print(stock_price)

#append object to the end of the list
stock_price.append(380)
print(stock_price)

#extend the array with another array
stock_price.extend([400,430,398,390,385,360])
print(stock_price)

#pop elements from the end of list
stock_price.pop(-2)
print(stock_price)

#give the array in the reverse order
stock_price.reverse()
print(stock_price)

#sort the array in ascending order
stock_price.sort(reverse = False)
print(stock_price)