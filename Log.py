class Log:
    month = ""
    number = 0
    msg = ""
    user = ""
    monthIndex = 0

    def __init__(self, month, number, msg, user):
        self.month = month
        self.number = number
        self.msg = msg
        self.user = user
        self.monthIndex = self.get_month_index()

    def get_month_index(self):
        months = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }
        return months.get(self.month, -1)

    def __str__(self):
        return f"Month: {self.month}, Log: {self.number}, Message: {self.msg}, User: {self.user}, MonthIdx: {self.get_month_index()}"