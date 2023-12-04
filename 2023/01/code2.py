import os
import re

folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, 'input.txt')
lines=[]
total=0

NUM_DICT = {
    "one": "1",
    "two" :"2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

STRING_LST = ["\d","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract_number_from_string(x):  
    string_parts = re.findall(r"(?=("+'|'.join(STRING_LST)+r"))", x)
    digits = [string_parts[0], string_parts[-1]]
    translated_digits = [d if d.isdigit() else NUM_DICT.get(d) for d in digits ]
    return int(''.join(translated_digits))

with open(filepath, 'r') as f:
    for line in f.readlines():
        total += extract_number_from_string(line)

print(total)