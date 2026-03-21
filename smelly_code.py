# Magic Numbers & Strings
def calculate_total(price):
    return price + (price * 0.15) + 20


# Long Function
def process_order(order):
    total = 0
    for item in order:
        total += item["price"] * item["quantity"]

    if total > 100:
        discount = total * 0.1
    else:
        discount = 0

    total -= discount

    print("Order Summary")
    for item in order:
        print(item["name"], item["quantity"], item["price"])

    print("Discount:", discount)
    print("Final Total:", total)

    if total > 200:
        print("Premium customer")
    else:
        print("Regular customer")


# Duplicate Code
def calculate_area_rectangle(length, width):
    area = length * width
    print("The area of rectangle is", area)
    return area

def calculate_area_square(side):
    area = side * side
    print("The area of square is", area)
    return area


# Large Class / God Object
class AppManager:
    def login(self, username, password):
        print("Logging in", username)

    def logout(self):
        print("Logging out")

    def process_payment(self, amount):
        print("Processing payment:", amount)

    def send_email(self, email):
        print("Sending email to", email)

    def generate_report(self):
        print("Generating report")

    def backup_data(self):
        print("Backing up data")


# Deeply Nested Conditionals
def check_access(user):
    if user["active"]:
        if user["role"] == "admin":
            if user["has_permission"]:
                return "Access granted"
            else:
                return "Permission denied"
        else:
            return "Not an admin"
    else:
        return "Inactive user"


# Commented-Out Code
def greet(name):
    # print("Old greeting system")
    # print("Welcome user")
    print("Hello", name)


# Inconsistent Naming
def calc(a, b, c):
    x = a * b
    y = x - c
    return y