from symbol_table import SymbolTable


class Parse:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.symbol_table = SymbolTable()

    def parse(self):
        self.current_token = self.lexer.get_next_token()
        self.program()

    def error(self, message):
        raise Exception(f"Error sintáctico: {message}")

    def eat(self, token_type):
        if self.current_token[0] == token_type:  # Cambio aquí para acceder al tipo de token
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Se esperaba {token_type} pero se encontró {self.current_token[0]}")  # Cambio aquí

    def program(self):
        # Regla inicial del programa
        # El EOF es para identificar el end of file.
        while self.current_token[0] != 'EOF':  # Cambio aquí para acceder al tipo de token
            if self.current_token[0] == 'INCLUDE':
                self.eat('INCLUDE')
            elif self.current_token[0] in ('TYPE'):  # Cambio aquí
                self.function_or_variable_declaration()
            elif self.current_token[0] == 'IF':  # Cambio aquí
                self.if_statement()
            else:
                self.error(f"Token inesperado: {self.current_token[0]}")  # Cambio aquí

    def variable_declaration(self):
        # Regla para la declaración de variables
        type = self.current_token[0]  # Tipo de la variable
        self.eat('TYPE')
        identifier = self.current_token[1]  # Nombre de la variable
        self.eat('ID')
        # Aquí puedes manejar el valor inicial si es necesario
        value = None
        self.eat('SEMICOLON')

        # Añadir a la tabla de símbolos
        self.symbol_table.add(identifier, type, value, self.lexer.line_number)

    def function_or_variable_declaration(self):
        self.eat('TYPE')  # Consume el tipo 

        if self.current_token[0] != 'ID':
            self.error("Se esperaba un identificador")

        self.eat('ID')  # Consume el identificador

        # Determina si es una declaración de función o una variable basándose en el token siguiente
        if self.current_token[0] == 'LPAREN':
            self.function_definition()
        elif self.current_token[0] == 'SEMICOLON':
            self.variable_declaration()
        else:
            self.error(f"Se esperaba LPAREN o SEMICOLON pero se encontró {self.current_token[0]}")

    def function_definition(self):
        self.symbol_table.enter_scope()  # Entrar en el ámbito de la función
        self.eat('LPAREN')  # Consume el paréntesis izquierdo
        
        # Manejar los argumentos de la función
        while self.current_token[0] != 'RPAREN':
            arg_type = self.current_token[0]
            self.eat(arg_type)  # Consume el tipo del argumento

            if self.current_token[0] == 'ID':
                arg_name = self.current_token[1]
                self.eat('ID')  # Consume el nombre del argumento

                # Registrar el argumento en la tabla de símbolos
                self.symbol_table.add(arg_name, arg_type, None, self.lexer.line_number)

        self.eat('RPAREN')  # Consume el paréntesis derecho
        self.eat('LBRACE')
        # Aquí manejarías el cuerpo de la función, incluyendo declaraciones de variables locales
        # ...

        self.eat('RBRACE')  # Consume la llave derecha que cierra el cuerpo de la función
        print(f"Añadido a la tabla de símbolos: {arg_name}, {arg_type}")
        self.symbol_table.exit_scope()  # Salir del ámbito de la función
        
