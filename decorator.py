#A decorator is just:
    #A function that adds extra behavior to another function without changing the original function's code

#Create a decorator (Security Guard: Check if the user is logged-in before performing sensitive actions)
# args and kwargs(keyword-arguments) allow the decorator to accept and forward any arguments required by the original function without knowing its exact signature
def authenticate(func):
    def wrapper(*args, **kwargs):
        print("Checking authentication...")
        user_logged_in = True

        if user_logged_in:
            print("Authentication successful")
            func(*args, **kwargs)
        else:
            print("Authentication failed")
    return wrapper

@authenticate  #same as: check_balance = authenticate(check_balance)
def check_balance():
    print("Your balance is Rs. 10,000")

@authenticate
def deposit_money(amount):
    print(f"{amount} deposited successfully")

@authenticate
def withdraw_money(amount, currency="INR"):
    print(f"{amount}{currency} withdrawn successfully")

check_balance()
deposit_money(100)
withdraw_money(200)