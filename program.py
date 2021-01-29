import sqlite3
from datetime import date
from datetime import datetime
import record
from record import Record

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE records (date DATE, description TEXT, amount REAL)")

choice = input("Add(a), View(v), or Quit(q)? ")
while choice in ["a", "A", "v", "V"]:
    if choice  in ["a", "A"]:
        currency_choice = input("MYR(m) or GBP(g) records? ")
        while currency_choice not in ["m", "M", "g", "G"]:
            currency_choice = input("Please enter m for MYR or g for GBP records: ")
        # open text file to write new spending records
        with open('/home/splicefire/Projects/Python/Finance/spendings.txt', 'a+') as reader:
            today = date.today().strftime("%d %b %Y") # date format i.e. 24 Jun 2021
            description = input("What did you spend on? ")
            # Takes as input a float and formats it into RMxx.xx/£xx.xx
            if currency_choice in ["m", "M"]:
                spended = "RM{:,.2f}".format(float(input("How much did you spend? (don't enter currency, i.e. 40.50): "))) 
            elif currency_choice in ["g", "G"]:
                spended = "£{:,.2f}".format(float(input("How much did you spend? (don't enter currency, i.e. 40.50): "))) 
            # Write to the text file i.e. (27 Jan 2021, description, RMxx.xx)
            # \r\n creates a new line, since we will read the entries line by line
            # the comma behind it separates the string, since later we will access individual components separated by comma
            reader.write(str(today) + ", " + description + ", " + spended + ", \r\n")
    elif choice in ["v", "V"]:
        currency_input = input("MYR(m)/GBP(g)/Both(b) records? ")
        while currency_input not in ["m", "M", "g", "G", "b", "B"]:
            currency_input = input("Please enter m for MYR, g for GBP records, or b for both records: ")
        if currency_input in ["b","B"]:
            currency_choice = "both"
        elif currency_input in ["m", "M"]:
            currency_choice = "MYR"
        elif currency_input in ["g", "G"]:
            currency_choice = "GBP"
        sum_myr = 0 
        sum_gbp = 0
        view_range = input("View weekly/monthly/all records? (w/m/a): ")
        # View this week's entries
        if view_range in ["w", "W"]:
            print("\n")
            print("Here are your recorded spendings this week")
            with open('/home/splicefire/Projects/Python/Finance/spendings.txt', 'r') as reader:
                line = reader.readline()
                while line != "":
                    entry = Record(*line.split(', '))
                    if entry.within_week() and (entry.currency == currency_choice or currency_choice == "both"):
                        print(entry.show())
                        if entry.currency == "MYR":
                            sum_myr += entry.amount
                        else:
                            sum_gbp += entry.amount
                    line = reader.readline()
        # To be added monthly entries
        elif view_range in ["m", "M"]:
            print("Nothing yet")
        # View all entries
        elif view_range in ["a", "A"]:
            print("\n")
            print("Here are all your recorded spendings")
            # Same as the above blocks, except we do not check date range of entries
            with open('/home/splicefire/Projects/Python/Finance/spendings.txt', 'r') as reader:
                line = reader.readline()
                while line != "":
                    entry = Record(*line.split(', '))
                    if entry.currency == currency_choice or currency_choice == "both":
                        print(entry.show())
                        if entry.currency == "MYR":
                            sum_myr += entry.amount
                        else:
                            sum_gbp += entry.amount
                    line = reader.readline()
        else:
            continue
        if currency_choice == "both":
            print("Total: " + str("RM{:,.2f}".format(sum_myr)) + "  " + str("£{:.2f}".format(sum_gbp)))
        elif currency_choice == "MYR":
            print("Total: " + str("RM{:,.2f}".format(sum_myr)))
        else:
            print("Total: " + str("£{:,.2f}".format(sum_gbp)))
        print("\n")

    choice = input("Add(a), View(v), or Quit(q)? ")
print("Program terminating...")
      

