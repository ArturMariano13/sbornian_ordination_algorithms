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
            "January": 0, "February": 1, "March": 2, "April": 3,
            "May": 4, "June": 5, "July": 6, "August": 7,
            "September": 8, "October": 9, "November": 10, "December": 11
        }
        return months.get(self.month, -1)

    def __str__(self):
        return f"Month: {self.month}, Log: {self.number}, Message: {self.msg}, User: {self.user}, MonthIdx: {self.get_month_index()}"
