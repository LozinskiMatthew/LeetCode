class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.calendar)):
            if (self.calendar[i][1] <= start or end <= self.calendar[i][0]) == False:
                return False
        self.calendar.append([start, end])
        return True