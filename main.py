import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_date, get_description, get_type

class CSV:
    FILE = "fincance_file.csv"
    COLUMNS = ["Date", "Type", "Amount", "Description"]


    @classmethod
    def create_csv(cls):
        try:
            pd.read_csv(cls.FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.FILE, index=False)

    @classmethod
    def add_entry(cls, date, type, amount, description):
        new_entry = {
            "Date" : date,
            "Type" : type,
            "Amount" : amount,
            "Description" : description
        }
        with open(cls.FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added succesfully")
    
def add_line():
    CSV.create_csv()
    date = get_date("Please enter date (format DD-MM-YYYY) or press enter to add today's date: ", allow_default=True)
    type = get_type("Please enter type(I for Income or E for Expense): ")
    amount = get_amount("Please enter the amount: ")
    description = get_description("Please write description (optional): ")
    CSV.add_entry(date, type, amount, description)

add_line()
