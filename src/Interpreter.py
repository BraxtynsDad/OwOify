# interpreter.py

from PyQt5.QtCore import QThread, pyqtSignal
import time  # For sleep in InterpreterThread

class Environment:
    def __init__(UwU):
        UwU.variables = {}
        UwU.functions = {}

    def set_variable(UwU, name, value):
        UwU.variables[name] = value

    def get_variable(UwU, name):
        if name in UwU.variables:
            return UwU.variables[name]
        else:
            raise NameError(f"Variable '{name}' is not defined.")

    def set_function(UwU, name, func_def):
        UwU.functions[name] = func_def

    def get_function(UwU, name):
        if name in UwU.functions:
            return UwU.functions[name]
        else:
            return None  # Return None if function is not defined

class Interpreter:
    def __init__(UwU, ast, interpreter_thread=None):
        UwU.ast = ast
        UwU.env = Environment()
        UwU.return_value = None  # To handle return statements
        UwU.interpreter_thread = interpreter_thread

    def interpret(UwU):
        try:
            for stmt in UwU.ast['statements']:
                UwU.execute_statement(stmt)
                if UwU.return_value is not None:
                    break  # Exit if a return statement is executed
        except Exception as e:
            error_message = f"Error: {e}"
            print(error_message)
            if UwU.interpreter_thread:
                UwU.interpreter_thread.output_signal.emit(error_message)

    def execute_statement(UwU, stmt):
        stmt_type = stmt['type']
        if stmt_type == 'variable_declaration':
            UwU.handle_variable_declaration(stmt)
        elif stmt_type == 'function_definition':
            UwU.handle_function_definition(stmt)
        elif stmt_type == 'function_call':
            UwU.handle_function_call(stmt)
        elif stmt_type == 'while_statement':
            UwU.handle_while_statement(stmt)
        elif stmt_type == 'if_statement':
            UwU.handle_if_statement(stmt)
        elif stmt_type == 'assignment':
            UwU.handle_assignment(stmt)
        elif stmt_type == 'return':
            UwU.return_value = UwU.evaluate_expression(stmt['value'])
        else:
            raise NotImplementedError(f"Statement type '{stmt_type}' not implemented.")

    def handle_variable_declaration(UwU, stmt):
        var_name = stmt['variable']
        var_type = stmt['var_type']
        value_node = stmt['value']
        value = UwU.evaluate_expression(value_node)

        # Enforce type based on var_type
        expected_type = {
            'nuu': int,
            'kawaii': float,
            'baka': bool,
            'pwease': str,
            'nyan': list,
        }

        if var_type in expected_type:
            try:
                value = expected_type[var_type](value)
            except ValueError:
                raise TypeError(f"Cannot assign value of type {type(value).__name__} to variable '{var_name}' of type {var_type}")
        else:
            raise TypeError(f"Unknown variable type '{var_type}'")

        UwU.env.set_variable(var_name, value)

    def handle_assignment(UwU, stmt):
        var_name = stmt['variable']
        value_node = stmt['value']
        value = UwU.evaluate_expression(value_node)
        if var_name in UwU.env.variables:
            UwU.env.set_variable(var_name, value)
        else:
            raise NameError(f"Variable '{var_name}' is not defined.")

    def evaluate_expression(UwU, expr):
        expr_type = expr['type']
        if expr_type == 'number':
            return float(expr['value']) if '.' in expr['value'] else int(expr['value'])
        elif expr_type == 'string':
            # Remove surrounding quotes
            return expr['value'].strip('"').strip("'")
        elif expr_type == 'boolean':
            val = expr['value']
            if val in ['Twue', 'twue']:
                return True
            elif val in ['Fawlse', 'fawlse']:
                return False
            else:
                raise ValueError(f"Invalid boolean value '{expr['value']}'")
        elif expr_type == 'identifier':
            return UwU.env.get_variable(expr['value'])
        elif expr_type == 'binary_operation':
            left = UwU.evaluate_expression(expr['left'])
            right = UwU.evaluate_expression(expr['right'])
            operator = expr['operator']
            return UwU.apply_operator(operator, left, right)
        elif expr_type == 'function_call':
            # Evaluate function call and return its result
            func_call_stmt = expr  # The expression is a function call statement
            return UwU.handle_function_call(func_call_stmt)
        elif expr_type == 'unary_operation':
            operator = expr['operator']
            operand = UwU.evaluate_expression(expr['operand'])
            if operator == 'nwope':
                return not operand
            else:
                raise NotImplementedError(f"Unary operator '{operator}' not implemented.")
        else:
            raise NotImplementedError(f"Expression type '{expr_type}' not implemented.")

    def apply_operator(UwU, operator, left, right):
        if operator == '+':
            # Handle string concatenation
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            else:
                return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            # Handle string multiplication
            if isinstance(left, str) and isinstance(right, int):
                return left * right
            elif isinstance(right, str) and isinstance(left, int):
                return right * left
            else:
                return left * right
        elif operator == '/':
            return left / right
        elif operator == '%':
            return left % right
        elif operator == '**':
            return left ** right
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
        elif operator == 'anwd':
            return left and right
        elif operator == 'owr':
            return left or right
        else:
            raise NotImplementedError(f"Operator '{operator}' not implemented.")

    def handle_function_definition(UwU, stmt):
        func_name = stmt['name']
        parameters = stmt['parameters']
        body = stmt['body']
        UwU.env.set_function(func_name, {'parameters': parameters, 'body': body})

    def handle_function_call(UwU, stmt):
        func_name = stmt['name']
        args = stmt['arguments']

        # Handle built-in functions
        if func_name == 'pwint':
            arg_values = [UwU.evaluate_expression(arg) for arg in args]
            output = ' '.join(map(str, arg_values))
            if UwU.interpreter_thread:
                UwU.interpreter_thread.output_signal.emit(output)
            else:
                print(output)
            return
        elif func_name == 'inpuwt':
            prompt = UwU.evaluate_expression(args[0]) if args else ''
            if UwU.interpreter_thread:
                user_input = UwU.interpreter_thread.get_input(prompt)
            else:
                user_input = input(prompt)
            return user_input
        elif func_name == 'leny':
            arg_value = UwU.evaluate_expression(args[0])
            return len(arg_value)
        elif func_name == 'wange':
            # Handle range function with 1 to 3 arguments
            arg_values = [UwU.evaluate_expression(arg) for arg in args]
            return range(*arg_values)
        elif func_name == 'inty':
            arg_value = UwU.evaluate_expression(args[0])
            return int(arg_value)
        elif func_name == 'stwie':
            arg_value = UwU.evaluate_expression(args[0])
            return str(arg_value)
        elif func_name == 'fwoaty':
            arg_value = UwU.evaluate_expression(args[0])
            return float(arg_value)
        elif func_name == 'booww':
            arg_value = UwU.evaluate_expression(args[0])
            return bool(arg_value)
        elif func_name == 'wistie':
            arg_values = [UwU.evaluate_expression(arg) for arg in args]
            return list(arg_values)
        else:
            # Handle user-defined functions
            func_def = UwU.env.get_function(func_name)
            if func_def is None:
                raise NameError(f"Function '{func_name}' is not defined.")

            # Evaluate arguments
            arg_values = [UwU.evaluate_expression(arg) for arg in args]

            # Prepare a new environment for function execution
            local_env = Environment()
            # Assign arguments to parameters
            for param, arg in zip(func_def['parameters'], arg_values):
                param_name = param['name']
                local_env.set_variable(param_name, arg)

            # Save current environment
            previous_env = UwU.env
            # Set the new local environment
            UwU.env = local_env

            # Execute function body
            return_value = None
            for s in func_def['body']:
                if s['type'] == 'return':
                    return_value = UwU.evaluate_expression(s['value'])
                    break
                else:
                    UwU.execute_statement(s)

            # Restore the previous environment
            UwU.env = previous_env

            return return_value

    def handle_if_statement(UwU, stmt):
        condition = UwU.evaluate_expression(stmt['condition'])
        if condition:
            for s in stmt['if_body']:
                UwU.execute_statement(s)
        else:
            for s in stmt.get('else_body', []):
                UwU.execute_statement(s)

    def handle_while_statement(UwU, stmt):
        condition = UwU.evaluate_expression(stmt['condition'])
        while condition:
            for s in stmt['body']:
                UwU.execute_statement(s)
            condition = UwU.evaluate_expression(stmt['condition'])

# InterpreterThread class within interpreter.py

class InterpreterThread(QThread):
    request_input = pyqtSignal(str)
    output_signal = pyqtSignal(str)

    def __init__(UwU, ast):
        super().__init__()
        UwU.ast = ast
        UwU.input_value = None
        UwU.input_received = False
        UwU.interpreter = Interpreter(ast, UwU)
        UwU._is_running = True

    ready_for_input = pyqtSignal()

    def run(UwU):
        try:
            UwU.interpreter.interpret()
            # Emit the signal when done
            UwU.ready_for_input.emit()
        except Exception as e:
            error_message = f"Interpreter Error: {e}"
            UwU.output_signal.emit(error_message)

    def get_input(UwU, prompt):
        UwU.request_input.emit(prompt)
        # Wait until input is received
        while not UwU.input_received and UwU._is_running:
            time.sleep(0.01)  # Sleep for a short time to prevent busy waiting
        if not UwU._is_running:
            raise Exception("Interpreter execution was stopped.")
        UwU.input_received = False
        return UwU.input_value

    def provide_input(UwU, value):
        UwU.input_value = value
        UwU.input_received = True

    def stop(UwU):
        UwU._is_running = False
