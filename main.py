'''Import modules'''
import csv
import pandas as pd
from data_entry import get_amount, get_date, get_description, get_category, get_currency

CURRENCIES = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNH", "HKD", "NZD", "PLN"]

class CSV:
    '''Class creates file or updates file by adding new row'''
    FILE = "fincance_file.csv"
    COLUMNS = ["Date", "Type", "Amount", "Currency", "Description"]

    @classmethod
    def create_csv(cls):
        '''Function to check if csv file exists and read file, otherwise create file'''
        try:
            pd.read_csv(cls.FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.FILE, index=False)

    @classmethod
    def add_entry(cls, date, category, amount, currency, description):
        '''Add new entry to csv file'''
        new_entry = {
            "Date" : date,
            "Type" : category,
            "Amount" : amount,
            "Currency" : currency,
            "Description" : description
        }
        with open(cls.FILE, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added succesfully")

def input_data():
    '''Funcion gets user input and adds new line to csv file'''
    CSV.create_csv()
    print("Welcome to Budget monitorin App!")
    date = get_date("Please enter date (format DD-MM-YYYY) or press enter to add today's date: ", allow_default=True)
    category = get_category("Please enter type(I for Income or E for Expense): ")
    amount = get_amount("Please enter the amount: ")
    if category == "Expense":
        amount *= -1
    currency = get_currency(f"Please enter currency code test {CURRENCIES}: ")
    description = get_description("Please write description (optional): ")
    CSV.add_entry(date, category, amount, currency, description)
    print(f"You have succesfully entered line to file with date: '{date}', category: '{category}', amount: '{amount}{currency}' and description: '{description}'")

input_data()
