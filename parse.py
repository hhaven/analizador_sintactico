##importar lexer

class Parse:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def parse(self):
        self.current_token = self.lexer.get_next_token()
        self.program()

    def error(self, message):
        raise Exception(f"Error sintáctico: {message}")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Se esperaba {token_type} pero se encontró {self.current_token.type}")

    def program(self):
        # Regla inicial del programa
        # El EOF es para identificar el end of file.
        while self.current_token.type != 'EOF':
            if self.current_token.type in ('INT', 'CHAR', 'FLOAT'):
                self.variable_declaration()
            elif self.current_token.type == 'VOID':
                self.function_definition()
            elif self.current_token.type == 'IF':
                self.if_statement()
            else:
                self.error(f"Token inesperado: {self.current_token.type}")
        print("Análisis sintáctico completado con éxito.")

    def variable_declaration(self):
        # Regla para la declaración de variables
        data_type = self.current_token
        self.eat(self.current_token.type)  # Consume el tipo de datos
        self.eat('ID')  # Consume el identificador de la variable
        self.eat('SEMI')  # Consume el punto y coma al final

    def function_definition(self):
        # Regla para la definición de funciones
        self.eat('VOID')  # Consume la palabra clave 'void'
        self.eat('ID')  # Consume el nombre de la función
        self.eat('LPAREN')  # Consume el paréntesis izquierdo
        # Puede incluir argumentos aquí
        self.eat('RPAREN')  # Consume el paréntesis derecho
        # Puede incluir el cuerpo de la función aquí
        self.eat('LBRACE')  # Consume la llave izquierda
        # Puede contener declaraciones de variables, instrucciones, etc.
        self.eat('RBRACE')  # Consume la llave derecha

    