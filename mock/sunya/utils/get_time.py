from datetime import datetime, timedelta


class GetTime:
    def __init__(self, initial_time=None, increment_in_seconds=1):
        if initial_time is None:
            self.current_time = datetime(2024, 1, 1)
        else:
            self.current_time = initial_time

        self.increment = timedelta(seconds=increment_in_seconds)

    def now(self, bump=False):
        result = self.current_time
        if bump:
            self.bump()
        return result

    def bump(self):
        self.current_time += self.increment
        return self.current_time


get_time = GetTime(increment_in_seconds=60)
