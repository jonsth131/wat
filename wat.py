import sys

from libwat import hash, encoding

INFO = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
END = "\033[0m"


def handle_result(result):
    if len(result) == 0:
        print(f"{RED}No match found{END}")
    else:
        print(f"{GREEN}Found {len(result)} match(es){END}")
        print(f'{GREEN}{"-" * 80}{END}')
        for h in result:
            if type(h) == tuple:
                print(f"{GREEN}{h[0]}: {h[1]}{END}")
            else:
                print(f"{GREEN}{h}{END}")
        print(f'{GREEN}{"-" * 80}{END}')


def is_hash(text):
    print(f"{INFO}Checking hashes...{END}", end="")
    try:
        hashes = hash.load_data()
    except FileNotFoundError:
        print(f"{RED}Could not load hash file, skipping hash check{END}")
        return

    print(f"{INFO}Loaded {len(hashes)} hashes...{END}", end="")
    result = hash.check_hash(hashes, text)
    handle_result(result)


def is_encoded(text):
    print(f"{INFO}Checking encodings...{END}", end="")
    result = encoding.test_all(text)
    handle_result(result)

    if len(result) == 0:
        return None

    return result


def run_all(text):
    is_hash(text)

    result = is_encoded(text)
    if result is not None:
        for (_, val) in result:
            if val == "":
                continue
            run_all(val)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Invalid arguments, usage: {sys.argv[0]} <string>")
        exit(-1)

    run_all(sys.argv[1])
