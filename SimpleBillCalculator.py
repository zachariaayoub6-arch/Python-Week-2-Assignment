#capturing the user input for price and quantity of an item
price = float (input("Enter the price of the item "))

quantity = int (input("Enter the quantity of the item "))

#calculating the total price of the item
total = price * quantity

#displaying the total price of the item
print(f"{quantity} Items at {price} each =  {total}")
