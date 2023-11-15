from lexer import lexer
from parse import parser
def main():
    file_path = "code.c"
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            lexer.input(source_code)
            parser.parse(source_code)
            print("Analisis sintactico completado con exito.")
            # Aquí puedes imprimir o trabajar con tu tabla de símbolos
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {file_path}")

if __name__ == "__main__":
    main()