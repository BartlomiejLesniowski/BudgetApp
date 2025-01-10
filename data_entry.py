from datetime import datetime

TYPES = {"I" : "Income",
        "E" : "Expense"
        }

def get_date():
    date_input = input("Please enter date (format DD-MM-YYYY) or press enter to add today's date ")

    try:
        valid_date = datetime.strptime(date_input, "%d-%m-%Y")
        return valid_date.strptime("%d-%m-%Y")
    except ValueError:
        print("Please enter valid format of the date: DD-MM-YYYY")


def get_type():
    type_input = input("Please enter type(I for Income or E for Expense) ").upper()
    if type in TYPES:
        return TYPES(type)
    else:
        print("Invalid type. Please enter I or E")
        return get_type



def get_amount(): 
    try:
        amount_input = float(input("Please enter the amount "))
        if amount_input <= 0:
            print("Please enter amount higher than 0")
        return amount_input
    except ValueError:
        print(ValueError)
        return get_amount

def get_description():
    desc_input = input("Please write description (optional) ")
    return desc_input