#!/usr/bin/python3

def read_file(filename=""):
    if filename.endswith(".txt"):
        with open(filename) as file:
            content = file.read()
            print(content, end="")
