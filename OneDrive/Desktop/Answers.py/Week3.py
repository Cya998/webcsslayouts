def calculate_discount (price, discount_percent):
    if discount_percent > 20: 
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price
    
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

print("Final price after discount: ", calculate_discount(price, discount_percent))



    
   