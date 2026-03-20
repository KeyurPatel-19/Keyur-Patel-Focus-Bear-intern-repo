def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    
    return price - (price * discount_percent / 100)