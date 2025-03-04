# 8. Your application receives temporal data in string format, but you want to convert those
# strings into datetime objects in order to perform nonstring operations on them.

from datetime import datetime

class DateConverter:
    def convertStringToDatetime(self, dateString, dateFormat):
        """Convert a string to a datetime object."""
        try:
            return datetime.strptime(dateString, dateFormat)
        except ValueError:
            return "Invalid date format"

dateConverter = DateConverter()

dateString1 = "2025-02-03 14:25:30"
dateFormat1 = "%Y-%m-%d %H:%M:%S"

dateString2 = "03/02/2025"
dateFormat2 = "%d/%m/%Y"

datetimeObj1 = dateConverter.convertStringToDatetime(dateString1, dateFormat1)
datetimeObj2 = dateConverter.convertStringToDatetime(dateString2, dateFormat2)

print("Converted datetime 1:", datetimeObj1)
print("Converted datetime 2:", datetimeObj2)
