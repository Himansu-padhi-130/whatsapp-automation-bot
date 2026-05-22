import pandas as pd

def load_contacts():
    data = pd.read_excel("contacts.xlsx")
    print(data)

load_contacts()