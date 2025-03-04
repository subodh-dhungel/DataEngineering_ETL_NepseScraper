# 9. You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. At
# what local time did your friend in Bangalore, India, have to show up to attend?

from datetime import datetime, timedelta

class TimeConverter:
    def convertCSTtoIST(self, cstTime):
        """Convert Chicago Time (CST) to Bangalore Time (IST)."""
        utcTime = cstTime + timedelta(hours=6)
        
        istTime = utcTime + timedelta(hours=5, minutes=30)
        return istTime

# Chicago time
chicagoTimeStr = "2012-12-21 09:30:00"
chicagoTimeFormat = "%Y-%m-%d %H:%M:%S"

chicagoTime = datetime.strptime(chicagoTimeStr, chicagoTimeFormat)

timeConverter = TimeConverter()
bangaloreTime = timeConverter.convertCSTtoIST(chicagoTime)

print(f"Chicago time: {chicagoTime}")
print(f"Bangalore time: {bangaloreTime}")
