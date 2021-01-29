from datetime import date
from datetime import datetime

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
        currency_choice = input("MYR(m)/GBP(g)/All(a) records? ")
        while currency_choice not in ["m", "M", "g", "G", "a", "A"]:
            currency_choice = input("Please enter m for MYR, g for GBP records, or a for all records: ")
        sum = 0 # Variable that stores sum of spending in a given period
        view_range = input("View weekly/monthly/all records? (w/m/a): ")
        # View this week's entries
        if view_range in ["w", "W"]:
            print("\n")
            print("Here are your recorded spendings this week")
            with open('/home/splicefire/Projects/Python/Finance/spendings.txt', 'r') as reader:
                line = reader.readline()
                # (1) split the line based on comma and store the components into list
                #        i.e.['27 Jan 2021', 'description', 'RMxx.xx', '\r\n'] (The last component is useless, do not print)
                # (2) compare spend_date with today's date (to see if it's within specified range)
                # (3) if the entry is within specified range:
                #     a) print the entry (line_list[0][0:6] basically just prints the day and month, and not the year)
                #     b) add the spent amount to the sum
                if currency_choice in ["a", "A"]:
                    sum_gbp = 0
                    while line != '':
                        line_list = line.split(', ')
                        spend_date = line_list[0]
                        datetime_obj = (datetime.strptime(spend_date, "%d %b %Y"))
                        if (date.today() - datetime_obj.date()).days <= 7:
                            print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                        if line_list[2][0:1] == "R":
                            sum += float(line_list[2][2:len(line_list[2])])
                        else:
                            sum_gbp += float(line_list[2][1:len(line_list[2])])
                        line = reader.readline()
                    print("Total: " + str("RM{:,.2f}".format(sum)) + "  " + str("£{:.2f}".format(sum_gbp)))
                elif currency_choice in ["m", "M"]:
                    while line != '':
                        line_list = line.split(', ')
                        if line_list[2][0:2] == "RM":
                            spend_date = line_list[0]
                            datetime_obj = (datetime.strptime(spend_date, "%d %b %Y"))
                            if (date.today() - datetime_obj.date()).days <= 7:
                                print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                            sum += float(line_list[2][2:len(line_list[2])])
                        line = reader.readline()
                    print("Total: " + str("RM{:,.2f}".format(sum)))
                elif currency_choice in ["g", "G"]:
                    while line != '':
                        line_list = line.split(', ')
                        if line_list[2][0:1] == "£":
                            spend_date = line_list[0]
                            datetime_obj = (datetime.strptime(spend_date, "%d %b %Y"))
                            if (date.today() - datetime_obj.date()).days <= 7:
                                print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                            sum += float(line_list[2][1:len(line_list[2])])
                        line = reader.readline()
                    print("Total: " + str("£{:,.2f}".format(sum)))
            print("\n")
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
                if currency_choice in ["a", "A"]:
                    sum_gbp = 0
                    while line != '':
                        line_list = line.split(', ')
                        print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                        if line_list[2][0:1] == "R":
                            sum += float(line_list[2][2:len(line_list[2])])
                        else:
                            sum_gbp += float(line_list[2][1:len(line_list[2])])
                        line = reader.readline()
                    print("Total: " + str("RM{:,.2f}".format(sum)) + "  " + str("£{:.2f}".format(sum_gbp)))
                elif currency_choice in ["m", "M"]:
                    while line != '':
                        line_list = line.split(', ')
                        if line_list[2][0:2] == "RM":
                            print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                            sum += float(line_list[2][2:len(line_list[2])])
                        line = reader.readline()
                    print("Total: " + str("RM{:,.2f}".format(sum)))
                elif currency_choice in ["g", "G"]:
                    while line != '':
                        line_list = line.split(', ')
                        if line_list[2][0:1] == "£":
                            print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                            sum += float(line_list[2][1:len(line_list[2])])
                        line = reader.readline()
                    print("Total: " + str("£{:,.2f}".format(sum)))
            print("\n")
        else:
            continue
    choice = input("Add(a), View(v), or Quit(q)? ")
print("Program terminating...")
      

