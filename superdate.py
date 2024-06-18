from datetime import datetime


class SuperDate(datetime):
    SEASONS = {
        'Winter': (12, 1, 2),
        'Spring': (3, 4, 5),
        'Summer': (6, 7, 8),
        'Autumn': (9, 10, 11),
    }

    TIMES_OF_DAY = {
        'Morning': range(6, 12),
        'Day': range(12, 18),
        'Evening': range(18, 24),
        'Night': range(0, 6),
    }

    def get_season(self):
        month = self.month
        for season, months in self.SEASONS.items():
            if month in months:
                return season

    def get_time_of_day(self):
        hour = self.hour
        for time_of_day, hours in self.TIMES_OF_DAY.items():
            if hour in hours:
                return time_of_day


a = SuperDate(2024, 6, 18, 17)
print(a.get_season())
print(a.get_time_of_day())
