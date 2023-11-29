from lexer import lexer
from parse import parse
def main():
    file_path = "code.c"
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            lexer.input(source_code)
            parse()
            print("Analisis sintactico completado con exito.")
            # imprimir tabla de simbolos
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {file_path}")

if __name__ == "__main__":
    main()