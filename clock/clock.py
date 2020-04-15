from datetime import datetime, timedelta, time

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.midnight = datetime.combine(datetime.today(), time.min)

    def __repr__(self):
        return '{:%H:%M}'.format(self.midnight + timedelta(hours=self.hour) + timedelta(minutes=self.minute))

    def __eq__(self, other):
        return self.__repr__() == other

    def __add__(self, minutes):
        self.minute += minutes
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        return self
