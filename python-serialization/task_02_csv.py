#!/usr/bin/python3
import csv
import json
"""Converting CSV Data to JSON Format"""


def convert_csv_to_json(filename):
    """Function that converts CSV filename in parameter to  JSON data"""
    try:
        with open(filename, "r", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append(row)

        with open("data.json", "w") as jsonfile:
            json.dump(data, jsonfile)

        return True

    except FileNotFoundError:
        return False
