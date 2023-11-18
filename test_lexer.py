import ply.lex as lex
from lexer import tokens
from lexer import lexer

def test_lexer(file_path):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            lexer.input(source_code)

            # Itera a través de los tokens generados por el lexer
            while True:
                token = lexer.token()
                if not token:
                    break  # Se alcanzó el final de la cadena de entrada
                print(f"Token: {token.type}, Valor: {token.value}, Línea: {token.lineno}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {file_path}")

if __name__ == "__main__":
    # Ejemplo de prueba del lexer con un archivo de entrada
    input_file = "code.c"
    test_lexer(input_file)
