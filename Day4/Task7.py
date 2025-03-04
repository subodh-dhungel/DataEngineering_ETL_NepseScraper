# 7. You want a general solution for finding a date for the last occurrence of a day of the
# week. Last Friday, for example.

from datetime import datetime, timedelta

class DateFinder:
    def __init__(self):
        self.weekdays = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }

    def getLastOccurrence(self, targetDay):
        """Find the date of the last occurrence of a specific weekday."""
        today = datetime.today()
        targetDayNum = self.weekdays.get(targetDay)
        
        if targetDayNum is None:
            return "Invalid day name"
        
        daysDifference = (today.weekday() - targetDayNum) % 7
        lastOccurrenceDate = today - timedelta(days=daysDifference)
        return lastOccurrenceDate.strftime('%Y-%m-%d')

dateFinder = DateFinder()

print("Last Friday:", dateFinder.getLastOccurrence("Friday"))

print("Last Monday:", dateFinder.getLastOccurrence("Monday"))
