import sqlite3
from datetime import date
from datetime import datetime

# Connection to sqlite3, will create database.db file if not exists
connection = sqlite3.connect("/home/splicefire/Projects/Python/Finance/database.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records (date TEXT, description TEXT, currency TEXT, amount TEXT)")

choice = input("Add(a), View(v), or Quit(q)? ")
while choice in ["a", "A", "v", "V"]:
    # Add entries
    if choice  in ["a", "A"]:

        currency_choice = input("MYR(m) or GBP(g) records? ")
        while currency_choice not in ["m", "M", "g", "G"]:
            currency_choice = input("Please enter m for MYR or g for GBP records: ")
        if currency_choice in ["m", "M"]:
            currency = "RM"
        elif currency_choice in ["g", "G"]:
            currency = " £"

        description = input("What did you spend on? ")
        spended = input("How much did you spend? (don't enter currency, i.e. 40.50): ") 

        # Insert into database
        entry_sql = "INSERT INTO records (date, description, currency, amount) VALUES (?, ?, ?, ?)"
        cursor.execute(entry_sql, (date.today(), description, currency, spended))
        connection.commit()
        print("\n")
    # View entries
    elif choice in ["v", "V"]:
        currency_input = input("MYR(m)/GBP(g)/Both(b) records? ")
        while currency_input not in ["m", "M", "g", "G", "b", "B"]:
            currency_input = input("Please enter m for MYR, g for GBP records, or b for both records: ")
        if currency_input in ["b","B"]:
            currency_choice = "both"
            execute_string = "SELECT date, description, currency, amount FROM records"
        elif currency_input in ["m", "M"]:
            currency_choice = "MYR"
            execute_string = "SELECT date, description, currency, amount FROM records WHERE currency = 'RM'"
        elif currency_input in ["g", "G"]:
            currency_choice = "GBP"
            execute_string = "SELECT date, description, currency, amount FROM records WHERE currency = ' £'"
        sum_myr = 0 
        sum_gbp = 0
        myr_string = "SELECT sum(amount) FROM records WHERE currency = 'RM'"
        gbp_string = "SELECT sum(amount) FROM records WHERE currency = ' £'"
        view_range = input("View weekly/monthly/all records? (w/m/a): ")
        # format query for selecting weekly entries 
        if view_range in ["w", "W"]:
            if "WHERE" not in execute_string:
                execute_string += " WHERE date >= date('now', '-7 days')"
            else:
                execute_string += " AND date >= date('now', '-7 days')"
            myr_string += " AND date >= date('now', '-7 days')"
            gbp_string += " AND date >= date('now', '-7 days')"
            print("\n")
            print("Here are your recorded spendings this week")
        # format query for selecting monthly entries 
        elif view_range in ["m", "M"]:
            if "WHERE" not in execute_string:
                execute_string += " WHERE strftime('%m', date) = strftime('%m', 'now')"
            else:
                execute_string += " AND strftime('%m', date) = strftime('%m', 'now')"
            myr_string += " AND strftime('%m', date) = strftime('%m', 'now')"
            gbp_string += " AND strftime('%m', date) = strftime('%m', 'now')"
            print("Here are your recorded spendings this month")
        # format query for selecting all entries 
        elif view_range in ["a", "A"]:
            print("\n")
            print("Here are all your recorded spendings")
        
        #Execute query and format output
        cursor.execute(execute_string)
        print("\n")
        formatted_result = [f"{datetime.strptime(date, '%Y-%m-%d').date().strftime('%d %b'):<12}{description:<50}{currency:>2} {'{:.2f}'.format(float(amount)):>5}" for date, description, currency, amount in cursor.fetchall()]
        date, description, price = "Date", "Description", "Price"
        print('\n'.join([f"{date:<12}{description:<50}{price:>5}"] + formatted_result))
        sum_myr = cursor.execute(myr_string).fetchone()[0]
        sum_gbp = cursor.execute(gbp_string).fetchone()[0]
        print("\n")

        # Show sum of output entries
        if currency_choice == "both":
            print("Total: " + str("RM{:,.2f}".format(sum_myr)) + "  " + str("£{:.2f}".format(sum_gbp)))
        elif currency_choice == "MYR":
            print("Total: " + str("RM{:,.2f}".format(sum_myr)))
        else:
            print("Total: " + str("£{:,.2f}".format(sum_gbp)))
        print("\n")

    choice = input("Add(a), View(v), or Quit(q)? ")
connection.close()
print("Program terminating...")
      

