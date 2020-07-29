import os
import re
import sys
import json


def replace_chars(string):
    data = string
    chars_to_relace = [
        '{{ __', ' }}', "('", '("',
        "')", '")',
    ]
    for char in chars_to_relace:
        data = data.replace(char, '')

    return data


def get_files_paths(folder):
    paths = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            paths.append(os.path.join(root, file))

    return paths


def remove_duplicates(data):
    result = {}
    for key, value in data.items():
        if value not in result.values():
            data[key] = value

    return data


def main():
    # Getting arguments
    args = []
    params = {}
    try:
        del sys.argv[0]
        args = sys.argv
    except IndexError as e:
        pass

    if args:
        params['folder'] = args[0]
        try:
            params['input'] = args[1]
            params['output'] = args[1] + '.output'
        except IndexError as e:
            pass

    # Loading input file
    if 'input' in params:
        try:
            with open(params['input']) as input_file:
                input_data = json.load(input_file)
        except ValueError as e:
            print('Input file format error')
            exit()

    # Finding matched pattern in files
    pattern = re.compile("{{ __\\(.*\\) }}")
    files = get_files_paths(params['folder'])
    founds = []
    result = {}
    for file in files:
        for i, line in enumerate(open(file)):
            for match in re.finditer(pattern, line):
                founds.append(replace_chars(match.group()))

        for found in founds:
            result[found] = ''

    # Removing duplicates in data
    result = remove_duplicates(result)
    if 'input' in params:
        for data in result:
            if data not in input_data:
                input_data[data] = ''

        with open(params['output'], 'w') as outfile:
            json.dump(input_data, outfile)

        print('Output file: ' + params['output'])
    else:
        print(result)


if __name__ == "__main__":
    main()
