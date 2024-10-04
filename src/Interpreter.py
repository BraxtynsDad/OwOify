from Parser import OwOParser

class Environment:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            raise NameError(f"Variable '{name}' is not defined.")

    def set_function(self, name, func_def):
        self.functions[name] = func_def

    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        else:
            raise NameError(f"Function '{name}' is not defined.")


class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()

    def interpret(self):
        try:
            for stmt in self.ast['statements']:
                self.execute_statement(stmt)
        except Exception as e:
            print(f"Error: {e}")

    def execute_statement(self, stmt):
        stmt_type = stmt['type']
        if stmt_type == 'variable_declaration':
            self.handle_variable_declaration(stmt)
        elif stmt_type == 'function_definition':
            self.handle_function_definition(stmt)
        elif stmt_type == 'function_call':
            self.handle_function_call(stmt)
        elif stmt_type == 'while_statement':
            self.handle_while_statement(stmt)
        elif stmt_type == 'if_statement':
            self.handle_if_statement(stmt)
        elif stmt_type == 'assignment':
            self.handle_assignment(stmt)
        else:
            raise NotImplementedError(f"Statement type '{stmt_type}' not implemented.")

    def handle_variable_declaration(self, stmt):
        var_name = stmt['variable']
        var_type = stmt['var_type']
        value_node = stmt['value']
        value = self.evaluate_expression(value_node)
        # Optionally, enforce type based on var_type
        # For simplicity, we'll ignore var_type
        self.env.set_variable(var_name, value)

    def handle_assignment(self, stmt):
        var_name = stmt['variable']
        value_node = stmt['value']
        value = self.evaluate_expression(value_node)
        if var_name in self.env.variables:
            self.env.set_variable(var_name, value)
        else:
            raise NameError(f"Variable '{var_name}' is not defined.")

    def evaluate_expression(self, expr):
        expr_type = expr['type']
        if expr_type == 'number':
            return float(expr['value']) if '.' in expr['value'] else int(expr['value'])
        elif expr_type == 'string':
            # Remove surrounding quotes
            return expr['value'].strip('"').strip("'")
        elif expr_type == 'boolean':
            val = expr['value'].lower()
            if val == 'twue':  # Handling the typo 'Twue'
                return True
            elif val == 'false':
                return False
            else:
                raise ValueError(f"Invalid boolean value '{expr['value']}'")
        elif expr_type == 'identifier':
            return self.env.get_variable(expr['value'])
        elif expr_type == 'binary_operation':
            left = self.evaluate_expression(expr['left'])
            right = self.evaluate_expression(expr['right'])
            operator = expr['operator']
            return self.apply_operator(operator, left, right)
        else:
            raise NotImplementedError(f"Expression type '{expr_type}' not implemented.")

    def apply_operator(self, operator, left, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<=':
            return left <= right
        elif operator == '>=':
            return left >= right
        else:
            raise NotImplementedError(f"Operator '{operator}' not implemented.")

    def handle_function_definition(self, stmt):
        func_name = stmt['name']
        parameters = stmt['parameters']
        body = stmt['body']
        self.env.set_function(func_name, {'parameters': parameters, 'body': body})

    def handle_function_call(self, stmt):
        func_name = stmt['name']
        args = stmt['arguments']
        func_def = self.env.get_function(func_name)
        if func_def is None:
            raise NameError(f"Function '{func_name}' is not defined.")

        # Evaluate arguments
        arg_values = [self.evaluate_expression(arg) for arg in args]

        # Prepare a new environment for function execution
        local_env = Environment()
        # Assign arguments to parameters
        for param, arg in zip(func_def['parameters'], arg_values):
            param_name = param['name']
            local_env.set_variable(param_name, arg)

        # Save current environment
        previous_env = self.env
        # Set the new local environment
        self.env = local_env

        # Execute function body
        for stmt in func_def['body']:
            self.execute_statement(stmt)

        # Restore the previous environment
        self.env = previous_env

    def handle_if_statement(self, stmt):
        condition = self.evaluate_expression(stmt['condition'])
        if condition:
            for s in stmt['if_body']:
                self.execute_statement(s)
        else:
            for s in stmt.get('else_body', []):
                self.execute_statement(s)

    def handle_while_statement(self, stmt):
        condition = self.evaluate_expression(stmt['condition'])
        while condition:
            for s in stmt['body']:
                self.execute_statement(s)
            condition = self.evaluate_expression(stmt['condition'])

class ExtendedInterpreter(Interpreter):
    def handle_function_call(self, stmt):
        func_name = stmt['name']
        args = stmt['arguments']
        if func_name == 'pwint':
            # Handle 'pwint' as a print statement
            arg_values = [self.evaluate_expression(arg) for arg in args]
            print(*arg_values)
            return
        # Otherwise, handle as normal function
        func_def = self.env.get_function(func_name)
        if func_def is None:
            raise NameError(f"Function '{func_name}' is not defined.")

        # Evaluate arguments
        arg_values = [self.evaluate_expression(arg) for arg in args]

        # Prepare a new environment for function execution
        local_env = Environment()
        # Assign arguments to parameters
        for param, arg in zip(func_def['parameters'], arg_values):
            param_name = param['name']
            local_env.set_variable(param_name, arg)

        # Save current environment
        previous_env = self.env
        # Set the new local environment
        self.env = local_env

        # Execute function body
        for stmt in func_def['body']:
            self.execute_statement(stmt)

        # Restore the previous environment
        self.env = previous_env
