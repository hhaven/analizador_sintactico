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


    #CONDINITIONALS
    def initConditional(self, condition, statements, start, end):
        self.condition = condition
        self.statement = statements
        self.start = start 
        self.end = end

    #WHILE
    def parse_while_statement(tokens): #tokens hace referencia a la lista de tokens
        while_token = tokens.pop(0)
         if while_token != "while":
            raise SyntaxError("Se esperaba la palabra clave 'while'")
        open_paren = tokens.pop(0)
            if open_paren != "(":
                raise SyntaxError("Se esperaba '(' después de 'while'")
    
        condition = parse_condition(tokens)
        close_paren = tokens.pop(0)
            if close_paren != ")":
                raise SyntaxError("Se esperaba ')' después de la condición")
        open_brace = tokens.pop(0)
            if open_brace != "{":
                raise SyntaxError("Se esperaba '{' después de la condición")
        statements = parse_statement_list(tokens)   

        close_brace = tokens.pop(0)
            if close_brace != "}":
             raise SyntaxError("Se esperaba '}' al final del bucle while")
        return WhileStatement(condition, statements)     

    def parse_condition(tokens):
        # Implementa la lógica para analizar la condición aquí
        # Por simplicidad, asumamos que solo hay un token en la condición (puede ser una implementación más compleja)
        return tokens.pop(0)
    def parse_statement_list(tokens):
        # Implementa la lógica para analizar la lista de declaraciones aquí
        # Por simplicidad, asumamos que solo hay un token en la lista de declaraciones (puede ser una implementación más compleja)
        return [tokens.pop(0)]

    #FOR     
    def parse_for_statement(tokens):
        for_token = tokens.pop(0)
        if for_token != "for":
            raise SyntaxError("Se esperaba la palabra clave 'for'")
            variable = tokens.pop(0)
            in_token = tokens.pop(0)
        #
        #if in_token != "in":
        #    raise SyntaxError("Se esperaba la palabra clave 'in'")  
        #start = tokens.pop(0)
        #to_token = tokens.pop(0)
        #if to_token != "to":
        #    raise SyntaxError("Se esperaba la palabra clave 'to'")
        #end = tokens.pop(0)
        #pen_brace = tokens.pop(0)
        if open_brace != "{":
            raise SyntaxError("Se esperaba '{' después de 'for'")
        statements = parse_statement_list(tokens)
        close_brace = tokens.pop(0)
        if close_brace != "}":
            raise SyntaxError("Se esperaba '}' al final del bucle for")
        return ForStatement(variable, start, end, statements)

        #DO-WHILE
    def parse_do_while_statement(tokens):
        do_token = tokens.pop(0)
        if do_token != "do":
            raise SyntaxError("Se esperaba la palabra clave 'do'")
    
        open_brace = tokens.pop(0)
        if open_brace != "{":
            raise SyntaxError("Se esperaba '{' después de 'do'")
    
        statements = parse_statement_list(tokens)
    
        close_brace = tokens.pop(0)
        if close_brace != "}":
            raise SyntaxError("Se esperaba '}' al final del bloque do")
    
        while_token = tokens.pop(0)
        if while_token != "while":
            raise SyntaxError("Se esperaba la palabra clave 'while'")
    
        open_paren = tokens.pop(0)
        if open_paren != "(":
            raise SyntaxError("Se esperaba '(' después de 'while'")
    
        condition = parse_condition(tokens)
    
        close_paren = tokens.pop(0)
        if close_paren != ")":
            raise SyntaxError("Se esperaba ')' después de la condición")
    
        # Crear y devolver la representación del bucle do-while
        return DoWhileStatement(statements, condition)
    