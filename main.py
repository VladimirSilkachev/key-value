import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
d = dict()


# Данная функция проверяет, является ли временный файл
#   пустым и если да, то создает в нем пустой словарь.
def check():
    with open(storage_path, 'r') as s:
        try:
            data = json.load(s)
        except json.decoder.JSONDecodeError:
            with open(storage_path, 'a') as f:
                json.dump({}, f)


#  Вывод значений по ключам из файла.
def tempo_out(key):
    with open(storage_path, 'r') as s:
        data = json.load(s)
        delimiter = ', '
        try:
            print(delimiter.join(data[key]))
        except KeyError:
            print('')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type=str, help='Ключи.', dest='key')
    parser.add_argument("--val", dest='val')
    args = parser.parse_args()
    parser.add_argument('-n', '--name', type=open, default=storage_path)
    if args.val is not None:
        d[args.key] = args.val
        with open(storage_path, 'r') as s:
            base_dict = json.load(s)
            if list(base_dict.keys()).count(args.key) != 0:         # Создание списка из значений
                a = base_dict[args.key]                             # в случае если ключи повторяются.
                base_dict[args.key] = []
                base_dict[args.key].append(a)
                base_dict[args.key].append(args.val)
                with open(storage_path, 'w') as f:
                    json.dump(base_dict, f)

            else:
                with open(storage_path, 'w') as f:
                    base_dict.update(d)
                    json.dump(base_dict, f)
    else:
        tempo_out(args.key)


check()
main()
