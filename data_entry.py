from datetime import datetime
from decimal import Decimal

DATE_FORMAT = "%d-%m-%Y"
TYPES = {"I" : "Income", "E" : "Expense"}

def get_date(prompt, allow_default=True):
    date_input = input("Please enter date (format DD-MM-YYYY) or press enter to add today's date: ")
    if allow_default and not date_input:
        return datetime.today().strftime(DATE_FORMAT)

    try:
        valid_date = datetime.strptime(date_input, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Please enter valid format of the date: DD-MM-YYYY")
        return get_date(prompt, allow_default)


def get_type(prompt):
    type_input = input("Please enter type(I for Income or E for Expense): ").upper()
    if type_input in TYPES:
        return TYPES[type_input]
    else:
        print("Invalid type. Please enter I or E")
        return get_type(prompt)


def get_amount(prompt): 
    try:
        amount_input = float(input("Please enter the amount: "))
        decimal_num = Decimal(str(amount_input))
        rounded_amount = decimal_num.quantize(Decimal('.00'))
        if rounded_amount <= 0:
            print("Please enter amount higher than 0")
        return rounded_amount
    except ValueError:
        print(ValueError)
        return get_amount(prompt)
    

def get_description(prompt):
    desc_input = input("Please write description (optional): ")
    return desc_input