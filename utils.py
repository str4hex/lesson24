import re
from typing import Generator


def read_file(file: str) -> Generator:

    with open(file, encoding='utf-8') as f:
        while True:
            try:
                line = next(f).rstrip().split(" ")[:9]
                yield " ".join(line)
            except StopIteration:
                break


def answer(cmd: str, value: str, files: str) -> str:

    if cmd == 'filter':
        res = filter(lambda x: value in x, read_file(files))
        return "\n".join(list(res))

    if cmd == 'map':
        res = map(lambda x: x.split(" ")[int(value)], list(read_file(files)))
        return "\n".join(list(res))

    if cmd == 'unique':
        res = set(read_file(files))
        return '\n'.join(res)

    if cmd == 'sort':
        res = sorted(read_file(files))
        return '\n'.join(res)

    if cmd == "limit":
        res = list(read_file(files))[:int(value)]
        return '\n'.join(res)

    if cmd == "regex":
        regex = re.compile(value)
        res = list(filter(lambda x: regex.search(x), read_file(files)))
        return '\n'.join(res)
