from lexer import OwOCustomLexer
from Funny import *
import re

class OwOParser:
    def __init__(UwU, tokens):
        UwU.tokens = tokens
        UwU.current_token = None
        UwU.position = 0
        UwU.errors = []
        UwU.ast = {'statements': [], 'errors': UwU.errors}
        UwU.next_token()  # Initialize with the first token

    def next_token(UwU):
        """Advance to the next token, skipping comments, whitespace, and newlines."""
        while UwU.position < len(UwU.tokens):
            UwU.current_token = UwU.tokens[UwU.position]
            UwU.position += 1
            token_type = UwU.current_token[0]
            # Skip comments, whitespace, and newlines
            if token_type in ['COMMENT', 'WHITESPACE', 'NEWLINE']:
                continue
            else:
                print(f"Current token: {UwU.current_token}")
                break
        else:
            UwU.current_token = None  # No more tokens left

    def eat(UwU, expected_type=None, expected_value=None):
        """Consume the current token if it matches the expected type and value, otherwise report an error."""
        if UwU.current_token is None:
            UwU.report_error("Unexpected end of input.")
            return

        token_type, token_value = UwU.current_token

        if expected_type is not None and expected_value is not None:
            if token_type == expected_type and token_value == expected_value:
                UwU.next_token()
            else:
                UwU.report_error(f"Expected {expected_type} '{expected_value}', but got {token_type} '{token_value}'")
                UwU.next_token()
        elif expected_type is not None:
            if token_type == expected_type:
                UwU.next_token()
            else:
                UwU.report_error(f"Expected {expected_type}, but got {token_type}")
                UwU.next_token()
        else:
            UwU.next_token()

    def report_error(UwU, message):
        """Report an error with the current token."""
        if UwU.current_token:
            error = {
                'message': message,
                'start': UwU.position - 1,  # Previous position is the source of the error
                'length': len(UwU.current_token[1]) if UwU.current_token else 1
            }
            UwU.errors.append(error)

    def parse(UwU):
        """Parse the tokens into an AST."""
        while UwU.current_token is not None:
            statement = UwU.statement()
            if statement:
                UwU.ast['statements'].append(statement)
        return UwU.ast

    def statement(UwU):
        """Determine what type of statement to parse."""
        if UwU.current_token is None:
            return None

        token_type, token_value = UwU.current_token

        if token_value in ['baka', 'pwease', 'nuu', 'kawaii', 'nyan']:
            return UwU.variable_declaration()
        elif token_value == 'dewf':
            return UwU.function_definition()
        elif token_value == 'ifflie':
            return UwU.if_statement()
        elif token_value == 'whiwile':
            return UwU.while_statement()
        else:
            return UwU.assignment_or_function_call()

    def variable_declaration(UwU):
        """Parse a variable declaration with a type."""
        var_type = UwU.current_token[1]
        UwU.eat('IDENTIFIER')  # Consume type keyword (e.g., 'nuu')

        if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER':
            variable_name = UwU.current_token[1]
            UwU.eat('IDENTIFIER')  # Consume variable name

            if UwU.current_token and UwU.current_token == ('OPERATOR', '='):
                UwU.eat('OPERATOR', '=')
                value = UwU.expression()
                return {
                    'type': 'variable_declaration',
                    'var_type': var_type,
                    'variable': variable_name,
                    'value': value
                }
            else:
                UwU.report_error(f"Expected '=' after variable name, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                return None
        else:
            UwU.report_error(f"Expected variable name after type, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
            return None

    def import_statement(UwU):
        """Parse an import statement."""
        UwU.eat('impowt')  # Consume 'impowt'

        if UwU.current_token and UwU.current_token[0].isidentifier():
            module_name = UwU.current_token[0]
            UwU.eat()  # Consume the module name
            return {'type': 'import', 'module': module_name}
        else:
            UwU.report_error(f"Expected module name after 'impowt', but got {UwU.current_token[0] if UwU.current_token else 'EOF'}")
            return None

    def function_definition(UwU):
        """Parse a function definition."""
        UwU.eat('dewf')  # Consume 'dewf'

        if UwU.current_token and UwU.current_token[0].isidentifier():
            function_name = UwU.current_token[0]
            UwU.eat()  # Consume the function name
        else:
            UwU.report_error(f"Expected function name, but got {UwU.current_token[0] if UwU.current_token else 'EOF'}")
            return None

        UwU.eat('(')  # Expect '('

        parameters = []
        while UwU.current_token and UwU.current_token[0] != ')':
            if UwU.current_token[0].isidentifier():
                param_name = UwU.current_token[0]
                UwU.eat()  # Consume parameter name

                # Handle default parameter value
                if UwU.current_token and UwU.current_token[0] == '=':
                    UwU.eat('=')
                    default_value = UwU.expression()
                    parameters.append({'name': param_name, 'default': default_value})
                else:
                    parameters.append({'name': param_name})

                if UwU.current_token and UwU.current_token[0] == ',':
                    UwU.eat(',')  # Consume commas between parameters
                elif UwU.current_token and UwU.current_token[0] != ')':
                    UwU.report_error(f"Expected ',' or ')' in parameter list, but got {UwU.current_token[0]}")
            else:
                UwU.report_error(f"Expected parameter name, but got {UwU.current_token[0]}")
                UwU.next_token()

        UwU.eat(')')  # Expect ')'
        UwU.eat(':')  # Expect ':'

        # Parse function body
        body = UwU.block()

        return {'type': 'function_definition', 'name': function_name, 'parameters': parameters, 'body': body}

    def block(UwU):
        """Parse a block of statements (e.g., function body, if body)."""
        statements = []
        # For simplicity, assume that a block is indented or delimited by newlines
        while UwU.current_token and UwU.current_token[0] != '\n' and UwU.current_token[0] != 'elswe':
            stmt = UwU.statement()
            if stmt:
                statements.append(stmt)
            else:
                UwU.next_token()
        return statements

    def return_statement(UwU):
        """Parse a return statement."""
        UwU.eat('wetuwn')  # Consume 'wetuwn'
        value = UwU.expression()  # Parse the expression to return
        return {'type': 'return', 'value': value}

    def assignment_or_function_call(UwU):
        """Parse either an assignment or a function call."""
        identifier = UwU.current_token[0]
        UwU.eat()  # Consume the identifier

        # Handle assignment
        if UwU.current_token and UwU.current_token[0] == '=':
            UwU.eat('=')  # Consume '='
            value = UwU.expression()  # Parse the expression on the right-hand side
            return {'type': 'assignment', 'variable': identifier, 'value': value}

        # Handle function call
        elif UwU.current_token and UwU.current_token[0] == '(':
            UwU.eat('(')  # Consume '('
            args = []

            # Parse function arguments until we encounter ')'
            while UwU.current_token and UwU.current_token[0] != ')':
                args.append(UwU.expression())  # Parse each argument
                if UwU.current_token and UwU.current_token[0] == ',':
                    UwU.eat(',')  # Consume commas between arguments
                elif UwU.current_token and UwU.current_token[0] != ')':
                    UwU.report_error(f"Expected ',' or ')' in argument list, but got {UwU.current_token[0]}")
            UwU.eat(')')  # Consume closing ')'

            return {'type': 'function_call', 'name': identifier, 'arguments': args}

        else:
            UwU.report_error(f"Expected '=' or '(' after identifier, but got {UwU.current_token[0] if UwU.current_token else 'EOF'}")
            return None

    def if_statement(UwU):
        """Parse an if statement."""
        UwU.eat('ifflie')  # Consume 'ifflie'
        condition = UwU.expression()  # Parse the condition expression
        UwU.eat(':')  # Expect ':'

        # Parse the if block
        if_body = UwU.block()

        # Check for 'elswe' clause
        else_body = []
        if UwU.current_token and UwU.current_token[0] == 'elswe':
            UwU.eat('elswe')
            UwU.eat(':')  # Expect ':'
            else_body = UwU.block()

        return {'type': 'if_statement', 'condition': condition, 'if_body': if_body, 'else_body': else_body}

    def while_statement(UwU):
        """Parse a while statement."""
        UwU.eat('whiwile')  # Consume 'whiwile'
        condition = UwU.expression()  # Parse the condition expression
        UwU.eat(':')  # Expect ':'

        # Parse the while block
        body = UwU.block()

        return {'type': 'while_statement', 'condition': condition, 'body': body}

    def lookup_function_definition(UwU, function_name):
        """Helper function to lookup the function definition."""
        for statement in UwU.ast['statements']:
            if statement['type'] == 'function_definition' and statement['name'] == function_name:
                return statement
        return None

    # Operator precedence levels
    precedence = {
        '==': 5,
        '!=': 5,
        '<': 5,
        '<=': 5,
        '>': 5,
        '>=': 5,
        '+': 10,
        '-': 10,
        '*': 20,
        '/': 20,
        '**': 30,
    }

    def expression(UwU, min_precedence=0):
        """Parse an expression with operator precedence."""
        if UwU.current_token is None:
            UwU.report_error("Unexpected end of input.")
            return None

        # Parse the left-hand side (lhs) operand
        lhs = UwU.primary()

        while UwU.current_token and UwU.current_token[0] in UwU.precedence and UwU.precedence[UwU.current_token[0]] >= min_precedence:
            op = UwU.current_token[0]
            op_precedence = UwU.precedence[op]
            UwU.eat(op)  # Consume the operator

            # Parse the right-hand side (rhs) operand
            rhs = UwU.expression(op_precedence + 1)
            lhs = {'type': 'binary_operation', 'operator': op, 'left': lhs, 'right': rhs}

        return lhs

    def primary(UwU):
        """Parse primary expressions."""
        if UwU.current_token is None:
            UwU.report_error("Unexpected end of input.")
            return None

        token = UwU.current_token

        # Numbers (integers and floats)
        if re.match(r'^\d+(\.\d*)?([eE][+-]?\d+)?$|^\.\d+([eE][+-]?\d+)?$', token[0]):
            value = token[0]
            UwU.eat()  # Consume the number
            return {'type': 'number', 'value': value}

        # Boolean literals
        elif token[0] in ['Twue', 'Fawlse']:
            value = token[0]
            UwU.eat()  # Consume the boolean literal
            return {'type': 'boolean', 'value': value}

        # Lists
        elif token[0] == '[':
            UwU.eat('[')  # Consume '['
            elements = []
            while UwU.current_token and UwU.current_token[0] != ']':
                elements.append(UwU.expression())
                if UwU.current_token and UwU.current_token[0] == ',':
                    UwU.eat(',')  # Consume ','
                elif UwU.current_token and UwU.current_token[0] != ']':
                    UwU.report_error(f"Expected ',' or ']' in list, but got {UwU.current_token[0]}")
            UwU.eat(']')  # Consume ']'
            return {'type': 'list', 'elements': elements}

        # Identifiers and function calls
        elif token[0].isidentifier():
            identifier = token[0]
            UwU.eat()  # Consume the identifier

            # Function call
            if UwU.current_token and UwU.current_token[0] == '(':
                UwU.eat('(')  # Consume '('
                args = []
                while UwU.current_token and UwU.current_token[0] != ')':
                    args.append(UwU.expression())
                    if UwU.current_token and UwU.current_token[0] == ',':
                        UwU.eat(',')  # Consume ','
                    elif UwU.current_token and UwU.current_token[0] != ')':
                        UwU.report_error(f"Expected ',' or ')' in argument list, but got {UwU.current_token[0]}")
                UwU.eat(')')  # Consume ')'
                return {'type': 'function_call', 'name': identifier, 'arguments': args}
            else:
                return {'type': 'identifier', 'value': identifier}

        # Strings
        elif token[0].startswith('"') or token[0].startswith("'"):
            value = token[0]
            UwU.eat()  # Consume the string
            return {'type': 'string', 'value': value}

        # Parenthesized expression
        elif token[0] == '(':
            UwU.eat('(')  # Consume '('
            expr = UwU.expression()
            UwU.eat(')')  # Consume ')'
            return expr

        else:
            UwU.report_error(f"Unexpected token {token[0]}")
            UwU.next_token()
            return None