# ATM functions decomposition

def transfer_money(amount, card_balance):
    """Transfer given amount of money to the account."""
    card_balance += amount
    # save new balance to the database
    return card_balance
 
def withdraw_money(amount, card_balance):
    """Withdraw given amount of money from the account."""
    card_balance -= amount
    # save new balance to the database
    return card_balance

def log_transaction(action, money, card_balance):
    if action in (TRANSFER, WITHDRAW):
        print(action + ": $", money)
    print("Current balance:", card_balance)

def move_money(action, money, card_balance):
    if action == TRANSFER:
        return transfer_money(money, card_balance)
    elif action == WITHDRAW:
        return withdraw_money(money, card_balance)
    elif action == DISPLAY:
        return card_balance
        
def get_amount_of_money(action):
    if action == DISPLAY:
        return 0.0
    money = input("Enter the sum of money to " + action + ": ")
    return float(money)
    
def make_transaction(action, card_balance):
    money = get_amount_of_money(action)
    card_balance = move_money(action, money, card_balance)
    log_transaction(action, money, card_balance)
    
card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")
 
# card_pin and card_balance are read from the database
 
if card_pin == input_pin:
    action = input("Enter desired action: ")
    make_transaction(action, card_balance)
else:
    print("Incorrect pin!")
