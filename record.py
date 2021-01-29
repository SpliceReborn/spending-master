from datetime import date, datetime
class Record:


    def __init__(self, date, description, amount, newline):
        self.date = date
        self.description = description
        if amount[0:1] == "R":
            self.amount = float(amount[2:])
            self.currency = "MYR"
        else:
            self.amount = float(amount[1:])
            self.currency = "GBP"


    def show(self):
        return (self.date + ": " + "Spent " + str(self.amount) + " on + " + self.description) 


    def within_week(self):
        datetime_obj = (datetime.strptime(self.date, "%d %b %Y"))
        if (date.today() - datetime_obj.date()).days <= 7:
            return True
        return False

