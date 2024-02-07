class Time:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.is_24_hour = True

    def __str__(self):
        if self.is_24_hour:
            return f'{self.hours}:{self.minutes:02}:{self.seconds:02}'
        else:
            if self.hours == 0:
                hours_to_show = 12
            elif 13 <= self.hours <= 23:
                hours_to_show = self.hours - 12
            else:
                hours_to_show = self.hours
            if self.hours < 12:
                am_or_pm = 'am'
            else:
                am_or_pm = 'pm'

    def toggle_24_hr(self):
        self.is_24_hour = not self.is_24_hour

    def increment_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.increment_minute()

    def increment_minute(self):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.increment_hour()

    def increment_hour(self):
        self.hours += 1
        if self.hours == 24:
            self.hours = 0


t = Time(19,40,0)
t.toggle_24_hr()
for i in range(2000000):
    print(t)
    t.increment_second()