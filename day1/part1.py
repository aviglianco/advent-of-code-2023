import re

FILEPATH = "input.in"


def get_calibration_value(line):
    calibration_value = line[0] + line[-1]
    return calibration_value


def filter_out_letters(line):
    line_without_letters = re.sub(r'[^0-9]', '', line)
    return line_without_letters


def get_sum_of_calibration_values(file):
    sum_of_calibration_values = 0

    for line in file:
        line_without_letters = filter_out_letters(line)
        calibration_value = get_calibration_value(line_without_letters)
        sum_of_calibration_values += int(calibration_value)

    return sum_of_calibration_values


def open_file(filepath):
    file = open("input.in", "r")

    return file


def main():
    file = open_file(FILEPATH)
    sum_of_calibration_values = get_sum_of_calibration_values(file)
    print(sum_of_calibration_values)


if __name__ == '__main__':
    main()
