import re

# Expresiones
token_patterns = [
    (r'\/\*[\s\S]*?\*\/', 'COMMENT_MULTILINE'),  # Token para comentarios multilínea "/* ... */"
    (r'\/\/[^\n]*', 'COMMENT_LINE'),  # Token para comentarios de línea "// ..."
    (r'if', 'IF'),  # Token para la palabra clave "if"
    (r'else', 'ELSE'),  # Token para la palabra clave "else"
    (r'while', 'WHILE'),  # Token para la palabra clave "while"
    (r'return', 'RETURN'),  # Token para la palabra clave "return"
    (r'class', 'CLASS'),  # Token para la palabra clave "class"
    (r'int|float|char|void', 'TYPE'),  # Token para tipos de datos (int, float, char, void)
    (r'\d+\.\d+[eE][+-]?\d+', 'DOUBLE'),  # Token para números de doble precisión en notación científica
    (r'\d+\.\d+', 'FLOAT'),         # Token para números de punto flotante
    (r'\d+', 'NUM'),                # Token para números enteros
    (r'\+', 'PLUS'),  # Token para el operador de suma "+"
    (r'-', 'MINUS'),  # Token para el operador de resta "-"
    (r'\*', 'TIMES'),  # Token para el operador de multiplicación "*"
    (r'/', 'DIVIDE'),  # Token para el operador de división "/"
    (r'\(', 'LPAREN'),  # Token para el paréntesis izquierdo "("
    (r'\)', 'RPAREN'),  # Token para el paréntesis derecho ")"
    (r'\{', 'LBRACE'),  # Token para la llave izquierda "{"
    (r'\}', 'RBRACE'),  # Token para la llave derecha "}"
    (r';', 'SEMICOLON'),  # Token para el punto y coma ";"
    (r',', 'COMMA'),  # Token para la coma ","
    (r'"[^"]*"', 'STRING'), # Token para cadenas de caracteres
    (r'=', 'ASSIGN'),      # Token para  "="
    (r'\+=', 'ADD_ASSIGN'), # Token para  "+="
    (r'-=', 'SUB_ASSIGN'), # Token para  "-="
    (r'>', 'GREATER_ASSIGN'), # Token para  "-="
    (r'<', 'LESSER_ASSIGN'), # Token para  "-="
    (r'#include\s*<.*?>', 'INCLUDE'), # Token para include
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),  # Token para identificadores
    (r'.', 'UNKNOWN'),
]
# Expresión regular para ignorar espacios en blanco y saltos de línea
ignore_pattern = r'[ \t\n]+'

# Leer codigo
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = self.tokenize(source_code)
        self.token_index = 0

    def tokenize(self, source_code):
        tokens = []
        position = 0
        while position < len(source_code):
            match = None
            # Ignorar espacios en blanco y saltos de línea
            ignore_regex = re.compile(ignore_pattern)
            ignore_match = ignore_regex.match(source_code, position)
            if ignore_match:
                position = ignore_match.end()
                continue

            for pattern, token_type in token_patterns:
                regex = re.compile(pattern)
                match = regex.match(source_code, position)
                if match:
                    value = match.group(0)
                    tokens.append((token_type, value))
                    position = match.end()
                    break

            if not match:
                raise SyntaxError(f"Token no válido en la posición {position}")
        return tokens

    def get_next_token(self):
        if self.token_index < len(self.tokens):
            token = self.tokens[self.token_index]
            self.token_index += 1
            return token
        return ('EOF', None)  # Retorna EOF cuando se alcanza el final del código fuente


# Leer código y agregar tokens a la tabla de símbolos
