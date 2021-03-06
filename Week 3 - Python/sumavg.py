"""
  Дан список измерений производительности системы, необходимо выполнить для них операции
  суммирования и нахождения средней арифметической. Операции находятся в той же таблице.
  Для одного и того же измерения всегда указана только одна операция - либо sum, либо avg
"""
import unittest

def compress(msmts):
    result = []
    prev = None
    k = 1

    for m in sorted(msmts, key=lambda k: k['text']):
        if prev is None:
            result.append({"text": m["text"], "time": m["time"]})
        elif prev["text"] != m["text"]:
            result[-1]["time"] /= k
            result.append({"text": m["text"], "time": m["time"]})
            k = 1
        else:
            result[-1]["time"] += m["time"]
            if m["operation"] == "sum":
                k = 1
            elif m["operation"] == "avg":
                k += 1
        prev = m
    return result


class TestPerfMethods(unittest.TestCase):
    def compare_measurements(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for m1 in expected:
            for m2 in actual:
                if m1["text"] == m2["text"]:
                    self.assertEqual(m1["time"], m2["time"], f"Wrong time for measurement {m1['text']}")

    def test_performance1(self):
        measurements = [
            {"text": "startup", "time": 3, "operation": "sum"},
            {"text": "startup", "time": 5, "operation": "sum"},
            {"text": "startup", "time": 1, "operation": "sum"},
            {"text": "block_time", "time": 10, "operation": "avg"},
        ]
        expected = [
            {"text": "startup", "time": 9},
            {"text": "block_time", "time": 10},
        ]
        actual = compress(measurements)
        self.compare_measurements(actual, expected)

    def test_performance2(self):
        measurements = [
            {"text": "startup", "time": 3, "operation": "sum"},
            {"text": "startup", "time": 5, "operation": "sum"},
            {"text": "block_time", "time": 10, "operation": "avg"},
            {"text": "startup", "time": 1, "operation": "sum"},
            {"text": "block_time", "time": 11, "operation": "avg"},
            {"text": "block_time", "time": 12, "operation": "avg"},
        ]
        expected = [
            {"text": "startup", "time": 9},
            {"text": "block_time", "time": 11},
        ]
        actual = compress(measurements)
        self.compare_measurements(actual, expected)

    def test_performance3(self):
        measurements = [
            {"text": "startup", "time": 0, "operation": "sum"},
            {"text": "startup", "time": 0, "operation": "sum"},
            {"text": "startup", "time": 0, "operation": "sum"},
            {"text": "block_time", "time": 0, "operation": "avg"},
            {"text": "block_time", "time": 0, "operation": "avg"},
            {"text": "block_time", "time": 0, "operation": "avg"},
        ]
        expected = [
            {"text": "startup", "time": 0},
            {"text": "block_time", "time": 0},
        ]
        actual = compress(measurements)
        self.compare_measurements(actual, expected)

    def test_performance4(self):
        measurements = [
            {"text": "startup", "time": 3, "operation": "sum"},
            {"text": "startup", "time": 5, "operation": "sum"},
            {"text": "startup", "time": -1, "operation": "sum"},
            {"text": "block_time", "time": 0, "operation": "avg"},
            {"text": "block_time", "time": 1, "operation": "avg"},
            {"text": "block_time", "time": -1, "operation": "avg"},
        ]
        expected = [
            {"text": "startup", "time": 7},
            {"text": "block_time", "time": 0},
        ]
        actual = compress(measurements)
        self.compare_measurements(actual, expected)

    def test_performance_empty(self):
        measurements = [
        ]
        expected = [
        ]
        actual = compress(measurements)
        self.compare_measurements(actual, expected)

    def test_performance_complex(self):
        measurements = [
            {"text": "ui", "time": 1, "operation": "sum"},
            {"text": "startup", "time": 3, "operation": "sum"},
            {"text": "startup", "time": 5, "operation": "sum"},
            {"text": "block_time", "time": 10, "operation": "avg"},
            {"text": "startup", "time": 1, "operation": "sum"},
            {"text": "block_time", "time": 12, "operation": "avg"},
            {"text": "ui", "time": 3, "operation": "sum"},
            {"text": "ui", "time": 5, "operation": "sum"},
            {"text": "fetch_data", "time": 11, "operation": "avg"},
            {"text": "fetch_data", "time": 12, "operation": "avg"},
            {"text": "fetch_data", "time": 13, "operation": "avg"},
            {"text": "block_time", "time": 11, "operation": "avg"},
            {"text": "fetch_data", "time": 14, "operation": "avg"},
        ]
        expected = [
            {"text": "startup", "time": 9},
            {"text": "ui", "time": 9},
            {"text": "block_time", "time": 11},
            {"text": "fetch_data", "time": 12.5},
        ]
        actual = compress(measurements)
        self.compare_measurements(actual, expected)




if __name__ == '__main__':
    unittest.main()