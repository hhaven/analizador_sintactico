class SymbolTableEntry:
    def __init__(self, identifier, type, value, line_number, scope):
        self.identifier = identifier
        self.type = type
        self.value = value
        self.line_number = line_number
        self.scope = scope

    def __str__(self):
        return f"{self.identifier}: {self.type}, Value: {self.value}, Line: {self.line_number}, Scope: {self.scope}"


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.scope_stack = ["global"]

    def add(self, identifier, type, value, line_number):
        scope = self.current_scope()
        self.symbols[identifier] = SymbolTableEntry(identifier, type, value, line_number, scope)

    def get(self, identifier):
        return self.symbols.get(identifier, None)

    def update(self, identifier, value):
        if identifier in self.symbols:
            self.symbols[identifier].value = value

    def remove(self, identifier):
        if identifier in self.symbols:
            del self.symbols[identifier]

    def enter_scope(self, scope_name):
        self.scope_stack.append(scope_name)

    def exit_scope(self):
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()

    def current_scope(self):
        return self.scope_stack[-1]

    def __str__(self):
        return "\n".join(str(entry) for entry in self.symbols.values())