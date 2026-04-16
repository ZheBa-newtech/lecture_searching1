from pathlib import Path
import json


def read_data(file_name, field):
    file_name_js = file_name
    with open(file_name_js, 'r') as js_file:
        data = json.load(js_file)
        data = dict(data)

    for dat in data:
        if field in data:
            return data[field]
        else:
            return None




# cwd_path = Path.cwd()
#file_path = cwd_path / file_name
#def main():
#pass
#if __name__ == 'main':
#main()

print(read_data(file_name='sequential.json', field='unordered_numbers'))