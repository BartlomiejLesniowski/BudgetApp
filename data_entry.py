'''Import modules'''
from datetime import datetime
from decimal import Decimal

DATE_FORMAT = "%d-%m-%Y"
TYPES = {"I" : "Income", "E" : "Expense"}
CURRENCIES = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNH", "HKD", "NZD", "PLN"]

def get_date(prompt, allow_default=True):
    '''Function to get date with default value as today's date'''
    date_input = input("Please enter date (format DD-MM-YYYY) or press enter to add today's date: ")
    if allow_default and not date_input:
        return datetime.today().strftime(DATE_FORMAT)

    try:
        valid_date = datetime.strptime(date_input, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Please enter valid format of the date: DD-MM-YYYY")
        return get_date(prompt, allow_default)

def get_category(prompt):
    '''Function to get type of input (Income or Expense)'''
    category_input = input("Please enter type('I' for Income or 'E' for Expense): ").upper()
    if category_input in TYPES:
        return TYPES[category_input]
    else:
        print("Invalid type. Please enter 'I' or 'E'")
        return get_category(prompt)

def get_amount(prompt):
    '''Function to get amount of input'''
    try:
        amount_input = float(input("Please enter the amount: "))
        decimal_num = Decimal(str(amount_input))
        rounded_amount = decimal_num.quantize(Decimal('.00'))
        if rounded_amount <= 0:
            print("Please enter amount higher than 0")
            return get_amount(prompt)
        return rounded_amount
    except ValueError:
        print(ValueError)
        return get_amount(prompt)

def get_currency(prompt):
    '''Function to get amount currency of input'''
    currency_input = input(f"Please enter currency code {CURRENCIES}: ").upper()
    if currency_input in CURRENCIES:
        return currency_input
    else:
        print(f"Please enter valid currency code from the list: {CURRENCIES}")
        return get_currency(prompt)

def get_description(prompt):
    '''Function to get description of input'''
    desc_input = input("Please write description (optional): ")
    return desc_input
