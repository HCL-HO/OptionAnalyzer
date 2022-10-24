from typing import List

import pyperclip


def get_text_from_file(path) -> List[str]:
    f = open(path, "r")
    sql = f.readlines()
    return sql


def get_text_from_file_in_str(path) -> str:
    return "".join(str(x) for x in get_text_from_file(path))


def write_output(result):
    write_output_to_file(result, "output.txt")


def write_output_to_file(result, file):
    print(result + "\n")
    output = open(file, "w+")
    output.write(result)
    output.close()


def load_array_from_file(COMPUTERS_FILE, DELIMINATOR) -> List[str]:
    return get_text_from_file_in_str(COMPUTERS_FILE).split(DELIMINATOR)


def dict_prettify(d, indent=0):
    result = ''
    for key, value in d.items():
        result += '\t' * indent + str(key)
        if isinstance(value, dict):
            result += '\n'
            result += dict_prettify(value, indent)
        else:
            result += '\t' * (indent + 1) + str(value) + '\n'

    return result
