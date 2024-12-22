def calculate_total_price(cart_items):
    if not cart_items:
        return "The cart is empty."

    total_price = sum(cart_items.values())
    
    if len(cart_items) > 5:
        total_price *= 0.9  
    
    return f"Total Price: {total_price}"

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

print(calculate_total_price(cart_items))
