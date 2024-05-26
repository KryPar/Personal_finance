import csv
import gspread
import time

MONTH = 'april'

file = f"transaction_{MONTH}.csv"

transactions = []

food ={"LIDL","COOP"}
clothes = {"ZALANDO"}
subscriptions_telecom = {"T-mobile","Patreon"}

def hsbcFin(file):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader: 
        
            if len(row) >= 3:  
                
                date = row[0]
                name = row[2].strip()  
                amount = float(row[1])
                category = 'other'
                if name in food:
                    category = "food"
                elif name in clothes:
                    category = "clothes"
                elif name in subscriptions_telecom:
                    category = "subscriptions_telecom"
                elif name == "RENT":
                    category = "rent"
                elif name == "SALARY":
                    category = "salary"
                elif int(row[1]) > 0 and category == "other":
                    category = "extra_income"
                transaction = (date,name,amount,category )
                transactions .append(transaction)
        return transactions


sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")
rows =hsbcFin(file)
for row in rows:
    wks.insert_row([row[0],row[1],row[2],row[3],], 8)
    time.sleep(2)



