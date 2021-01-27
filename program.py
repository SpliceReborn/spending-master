from datetime import date
from datetime import datetime

choice = input("Add(a), View(v), or Quit(q)? ")
while choice in ["a", "A", "v", "V"]:
    if choice  in ["a", "A"]:
        # open a file to write to it, you have to specify the file path 
        # a in 'a+' stands for append to existing file, and the + stands for create file if not exist
        with open('/home/splicefire/Projects/Python/Finance/spendings.txt', 'a+') as reader:
            today = date.today().strftime("%d %b %Y") # date in the format dd mmm yyyy, i.e. 24 Jun 2021
            description = input("What did you spend on? ")
            # Takes as input a float and formats it into RMxx.xx
            spended = "RM{:,.2f}".format(float(input("How much did you spend? (don't enter currency, i.e. 40.50): "))) 
            # Write to the text file i.e. (27 Jan 2021, description, RMxx.xx)
            # \r\n creates a new line, since we will read the entries line by line
            # the comma behind it separates the string, since later we will access individual components separated by comma
            reader.write(str(today) + ", " + description + ", " + spended + ", \r\n")
    elif choice in ["v", "V"]:
        sum = 0 # Variable that stores sum of spending in a given period
        view_range = input("View weekly/monthly/all records? (w/m/a): ")
        # View this week's entries
        if view_range in ["w", "W"]:
            print("\n")
            print("Here are your recorded spendings this week")
            with open('/home/splicefire/Projects/Python/Finance/spendings.txt', 'r') as reader:
                # store the first line in 'line' variable
                line = reader.readline()
                # while line is not empty
                # (1) split the line based on comma and store the components into list, i.e.['27 Jan 2021', 'description', 'RMxx.xx']
                # (2) assign the first component to variable spend_date
                #     since spend_date is now in the string form, we turn it into a datetime_object
                #     so that we can compare it to today's date (to see if it's within specified range)
                # (3) if the entry is within specified range:
                #     a) print the entry (line_list[0][0:6] basically just prints the day and month, and not the year)
                #         Notice we prine line_list[2] first instead of line_list[1], so that's why we separate the \r\n into another component - line_list[3]
                #         If not we will print out an empty line which is ugly, you can of course modify it to your preferences
                #     b) add the spent amount to the sum
                # (4) read next line
                while line != '':
                    line_list = line.split(', ')
                    spend_date = line_list[0]
                    datetime_obj = (datetime.strptime(spend_date, "%d %b %Y"))
                    if (date.today() - datetime_obj.date()).days <= 7:
                        print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                    sum += float(line_list[2][2:len(line_list[2])])
                    line = reader.readline()
            print("Total: " + str("RM{:,.2f}".format(sum)))
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
                while line != '':
                    line_list = line.split(', ')
                    print(line_list[0][0:6] + ": " +  "Spent " + line_list[2] + " on " + line_list[1])
                    line = reader.readline()
                    sum += float(line_list[2][2:len(line_list[2])])
            print("Total: " + str("RM{:,.2f}".format(sum)))
            print("\n")
        else:
            continue
    choice = input("Add(a), View(v), or Quit(q)? ")
print("Program terminating...")
      

