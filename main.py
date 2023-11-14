from lexer import Lexer
from parse import Parse
from symbol_table import SymbolTable

def main():
    file_path = "code.c"
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            lexer = Lexer(source_code)
            parser = Parse(lexer)
            parser.parse()
            print("Análisis sintáctico completado con éxito.")
            print("Tabla de Símbolos:")
            print(parser.symbol_table)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {file_path}")
    except Exception as e:
        print(f"Se encontró un error durante el análisis: {e}")

if __name__ == "__main__":
    main()