def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price,discount)

    print("The final price is:",final_price)
except ValueError:
    print("Please enter valid numbers for price and discount.")
