import re
from itertools import combinations

FILEPATH = "input.in"

DIGIT_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value(line: str) -> str:
    calibration_value = line[0] + line[-1]
    return calibration_value


def get_all_substrings(string: str) -> [str]:
    res = [string[x:y] for x, y in combinations(
        range(len(string) + 1), r=2)]

    return res


def find_digits_in_substring_list(substring: [str]) -> [str]:
    digits = []

    for element in substring:
        if element in DIGIT_MAPPING:
            digits.append(DIGIT_MAPPING[element])
        elif element in DIGIT_MAPPING.values():
            digits.append(element)

    return digits


def get_sum_of_calibration_values(file: 'TextIOWrapper') -> int:
    sum_of_calibration_values = 0

    for line in file:
        substrings = get_all_substrings(line)
        digits = find_digits_in_substring_list(substrings)
        calibration_value = get_calibration_value(digits)
        sum_of_calibration_values += int(calibration_value)

    return sum_of_calibration_values


def open_file_readonly(filepath: str) -> 'TextIOWrapper':
    file = open(filepath, "r")

    return file


def main():
    file = open_file_readonly(FILEPATH)
    sum_of_calibration_values = get_sum_of_calibration_values(file)
    print(sum_of_calibration_values)


if __name__ == '__main__':
    main()
