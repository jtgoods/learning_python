# this program takes user input for two items, prices, and quantities, and delivers a calculated receipt of item, prices, and quantity, including the total cart cost
def item_total(price, qty): #function for total individual price
    return price * qty

def overall(b1, b2): #function for total cart price
    return b1 + b2
   
item1 = input("What kind of item would you like?") 
price1 = float(input("How much does it cost?")) 
qty1 = float(input("How many would you like?"))

item2 = input("What kind of item would you like next?") 
price2 = float(input("How much does it cost?")) 
qty2 = float(input("How many would you like?"))

total1 = item_total(price1, qty1)
total2 = item_total(price2, qty2)

print(f"Item:     {item1}")
print(f"Price:    ${price1:.2f}")
print(f"Quantity: {qty1}")
print(f"Total price: ${total1:.2f}")
print("-" * 24)
print(f"Item:     {item2}")
print(f"Price:    ${price2:.2f}")
print(f"Quantity: {qty2}")
print(f"Total price: ${total2:.2f}")
print("#" * 20)
print(f"Total cart price: ${overall(total1, total2):.2f}")
print("#" * 20)
