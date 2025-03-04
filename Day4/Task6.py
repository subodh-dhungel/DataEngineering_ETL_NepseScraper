# 6. You have code that needs to perform simple time conversions, like days to seconds,
# hours to minutes, and so on.

class TimeConverter:
    def daysToSeconds(self, days):
        """Convert days to seconds."""
        return days * 24 * 60 * 60

    def hoursToMinutes(self, hours):
        """Convert hours to minutes."""
        return hours * 60

    def minutesToSeconds(self, minutes):
        """Convert minutes to seconds."""
        return minutes * 60

    def secondsToHours(self, seconds):
        """Convert seconds to hours."""
        return seconds / 3600

    def hoursToDays(self, hours):
        """Convert hours to days."""
        return hours / 24

converter = TimeConverter()

print("5 Days to Seconds:", converter.daysToSeconds(5))
print("3 Hours to Minutes:", converter.hoursToMinutes(3))
print("120 Minutes to Seconds:", converter.minutesToSeconds(120))
print("7200 Seconds to Hours:", converter.secondsToHours(7200))
print("48 Hours to Days:", converter.hoursToDays(48))