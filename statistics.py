import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = Counter(self.data)
        mode_value = max(freq, key=freq.get)
        return (mode_value, freq[mode_value])

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        return math.sqrt(self.var())

    def freq_dist(self):
        freq = Counter(self.data)
        total = self.count()
        result = []

        for value, count in freq.items():
            percentage = (count / total) * 100
            result.append((round(percentage, 1), value))

        return sorted(result, key=lambda x: x[0], reverse=True)

    def describe(self):
        return f"""Count: {self.count()}
Sum: {self.sum()}
Min: {self.min()}
Max: {self.max()}
Range: {self.range()}
Mean: {round(self.mean())}
Median: {self.median()}
Mode: {self.mode()}
Variance: {round(self.var(),1)}
Standard Deviation: {round(self.std(),1)}
Frequency Distribution: {self.freq_dist()}"""