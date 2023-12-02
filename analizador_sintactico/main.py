from lexer import lexer
from parse import parse, symbol_table_print
def main():
    file_path = "code.c"
    try:
        f = open(file_path, 'r')
        code = f.read()
        parse(code)
        symbol_table_print()
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {file_path}")

if __name__ == "__main__":
    main()