import sys

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cli.py <path_to_ant_print_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = read_file(file_path)
    print(content)