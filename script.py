import argparse
import csv
from collections import defaultdict
import statistics
from tabulate import tabulate
import os

def read_files(files):
    result = defaultdict(list)
    for file in files:
        if not os.path.exists(file):
            print(f"Файл {file} не найден.")
            exit(1)
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row['student']
                result[key].append(float(row["coffee_spent"]))
    return result

class BaseReport:
    headers = []

    def calculate(self, data):
        raise NotImplementedError("")

class MedianCoffeeReport(BaseReport):
    headers = ["Student", "Median Coffee"]

    def calculate(self, data):
        result = {}
        for key, values in data.items():
            result[key] = statistics.median(values)
        return dict(sorted(result.items(),key=lambda x: x[1], reverse=True))

REPORTS = {
    "median-coffee": MedianCoffeeReport(),
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+')
    parser.add_argument('--report')
    args = parser.parse_args()
    if args.report not in REPORTS:
        print(f"Отчет '{args.report}' не найден. Доступные: {list(REPORTS.keys())}")
        exit(1)

    data = read_files(files=args.files)
    report = REPORTS[args.report]
    result = report.calculate(data)
    print(tabulate(result.items(), headers=report.headers, tablefmt="grid"))