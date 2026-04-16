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
def linear_search(sekvenc, cislo):
    positions = []
    for i in range(len(sekvenc)):
        if sekvenc[i] == cislo:
            positions.append(i)
    return {'positions': positions, 'count': len(positions)}

# print(read_data(file_name='sequential.json', field='unordered_numbers'))


def binary_search(seznam, cislo):
    for index, value in enumerate(seznam):
        if value == cislo:
            return index
    return None

    # for sez in seznam:
    #     i += 1
    #     while sez != cislo:
    #         return None
    #     if sez == cislo:
    #         return i
    # #     if sez == cislo:
    # #         return i
    # #     else:
    # #         return None
print(binary_search(seznam=read_data(file_name='sequential.json', field='unordered_numbers'), cislo = 17))
# print(linear_search(sekvenc=read_data(file_name='sequential.json', field='unordered_numbers'), cislo=5))