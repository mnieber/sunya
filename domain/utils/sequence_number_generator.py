class SequenceNumberGenerator:
    def __init__(self):
        self._sequence_number = 0

    def next(self):
        self._sequence_number += 1
        return self._sequence_number
