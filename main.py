import pandas as pd
import csv
from datetime import datetime

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
    

