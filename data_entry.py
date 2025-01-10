from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"

TYPES = {"I" : "Income",
        "E" : "Expense"
        }

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
    if type in TYPES:
        return TYPES(type)
    else:
        print("Invalid type. Please enter I or E")
        return get_type



def get_amount(prompt): 
    try:
        amount_input = float(input("Please enter the amount: "))
        if amount_input <= 0:
            print("Please enter amount higher than 0")
        return amount_input
    except ValueError:
        print(ValueError)
        return get_amount

def get_description(prompt):
    desc_input = input("Please write description (optional): ")
    return desc_input