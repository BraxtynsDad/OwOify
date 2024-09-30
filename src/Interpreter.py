class Interpreter:
    def __init__(self):
        self.environment = {}  # Store variables and functions

    def evaluate(self, node):
        node_type = node['type']
        if node_type == 'number':
            return int(node['value'])
        elif node_type == 'string':
            return node['value']
        elif node_type == 'identifier':
            return self.environment[node['value']]
        elif node_type == 'binary_operation':
            left = self.evaluate(node['left'])
            right = self.evaluate(node['right'])
            operator = node['operator']
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            # Add other operators as needed
        elif node_type == 'function_call':
            function_name = node['name']
            arguments = [self.evaluate(arg) for arg in node['arguments']]
            return self.call_function(function_name, arguments)
        elif node_type == 'assignment':
            var_name = node['variable']
            value = self.evaluate(node['value'])
            self.environment[var_name] = value
        # Add more node types as needed (e.g., function definitions, returns)

    def call_function(self, function_name, arguments):
        if function_name == 'pwint':
            print(*arguments)
        # Handle other built-in or user-defined functions here