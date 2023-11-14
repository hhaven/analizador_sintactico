class SymbolTableEntry:
    def __init__(self, identifier, type, value, line_number, scope):
        self.identifier = identifier
        self.type = type
        self.value = value
        self.line_number = line_number
        self.scope = scope

    def __str__(self):
        return f"Identifier: {self.identifier}, Type: {self.type}, Value: {self.value}, Line: {self.line_number}, Scope: {self.scope}"


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.scope_stack = ["global"]

    def add(self, identifier, type, value, line_number):
        scope = self.current_scope()
        if identifier not in self.symbols:
            self.symbols[identifier] = SymbolTableEntry(identifier, type, value, line_number, scope)
        else:
            # Manejar redeclaraciones o actualizaciones
            pass

    def get(self, identifier):
        return self.symbols.get(identifier, None)

    def enter_scope(self):
        # Crea un nuevo ámbito (por ejemplo, al entrar en un bloque de función)
        new_scope = f"scope_{len(self.scope_stack)}"
        self.scope_stack.append(new_scope)

    def exit_scope(self):
        # Sale del ámbito actual
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()

    def current_scope(self):
        # Devuelve el ámbito actual
        return self.scope_stack[-1]

    def __str__(self):
        return "\n".join(str(entry) for entry in self.symbols.values())