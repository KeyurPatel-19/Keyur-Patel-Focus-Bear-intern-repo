# Constants for magic numbers and strings
TAX_RATE = 0.15
SHIPPING_FEE = 20
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.10
PREMIUM_THRESHOLD = 200


def calculate_total(price):
    return price + (price * TAX_RATE) + SHIPPING_FEE


# Refactored long function into smaller functions
def calculate_order_subtotal(order):
    subtotal = 0
    for item in order:
        subtotal += item["price"] * item["quantity"]
    return subtotal


def calculate_discount(subtotal):
    if subtotal > DISCOUNT_THRESHOLD:
        return subtotal * DISCOUNT_RATE
    return 0


def print_order_summary(order):
    print("Order Summary")
    for item in order:
        print(item["name"], item["quantity"], item["price"])


def get_customer_type(final_total):
    if final_total > PREMIUM_THRESHOLD:
        return "Premium customer"
    return "Regular customer"


def process_order(order):
    subtotal = calculate_order_subtotal(order)
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount

    print_order_summary(order)
    print("Discount:", discount)
    print("Final Total:", final_total)
    print(get_customer_type(final_total))


# Refactored duplicate code
def calculate_area(shape_name, area):
    print(f"The area of {shape_name} is {area}")
    return area


def calculate_area_rectangle(length, width):
    return calculate_area("rectangle", length * width)


def calculate_area_square(side):
    return calculate_area("square", side * side)


# Refactored large class into smaller classes
class UserAuth:
    def login(self, username, password):
        print("Logging in", username)

    def logout(self):
        print("Logging out")


class PaymentProcessor:
    def process_payment(self, amount):
        print("Processing payment:", amount)


class NotificationService:
    def send_email(self, email):
        print("Sending email to", email)


class ReportService:
    def generate_report(self):
        print("Generating report")

    def backup_data(self):
        print("Backing up data")


# Refactored deeply nested conditionals
def check_access(user):
    if not user["active"]:
        return "Inactive user"
    if user["role"] != "admin":
        return "Not an admin"
    if not user["has_permission"]:
        return "Permission denied"
    return "Access granted"


# Removed commented-out code
def greet(name):
    print("Hello", name)


# Improved naming
def calculate_remaining_amount(price, quantity, discount):
    total_price = price * quantity
    remaining_amount = total_price - discount
    return remaining_amount