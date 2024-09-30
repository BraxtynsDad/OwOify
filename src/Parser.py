# parser.py

from lexer import OwOCustomLexer  # Assuming you have a lexer module
from Funny import *  # Assuming this module contains necessary definitions

import logging

logging.basicConfig(level=logging.DEBUG)

class OwOParser:
    def __init__(UwU, tokens):
        """
        Initialize the parser with a list of tokens.

        Args:
            tokens (list): A list of tuples representing tokens.
        """
        UwU.tokens = tokens
        UwU.current_token = None
        UwU.position = 0
        UwU.errors = []
        UwU.ast = {'statements': [], 'errors': UwU.errors}
        UwU.next_token()  # Initialize with the first token

    def next_token(UwU):
        while UwU.position < len(UwU.tokens):
            UwU.current_token = UwU.tokens[UwU.position]
            UwU.position += 1
            token_type = UwU.current_token[0]
            # Skip comments and whitespace
            if token_type in ['COMMENT', 'WHITESPACE', 'NEWLINE']:
                continue
            elif token_type == 'UNKNOWN':
                UwU.report_error(f"Unknown token '{UwU.current_token[1]}'")
                continue  # Skip unknown tokens
            else:
                break
        else:
            UwU.current_token = None  # No more tokens
        logging.debug(f"Next token: {UwU.current_token}")

    def current_token_is(UwU, expected_type, expected_value=None):
        if UwU.current_token is None:
            return False
        token_type, token_value, _, _ = UwU.current_token
        if token_type != expected_type:
            return False
        if expected_value is not None and token_value != expected_value:
            return False
        return True

    def eat(UwU, expected_type=None, expected_value=None):
        if UwU.current_token is None:
            UwU.report_error("Unexpected end of input.")
            return

        token_type, token_value, _, _ = UwU.current_token

        if expected_type is not None:
            if token_type == expected_type:
                if expected_value is not None:
                    if token_value == expected_value:
                        UwU.next_token()
                    else:
                        UwU.report_error(
                            f"Expected {expected_type} '{expected_value}', but got {token_type} '{token_value}'")
                        UwU.next_token()
                else:
                    UwU.next_token()
            else:
                UwU.report_error(f"Expected {expected_type}, but got {token_type}")
                UwU.next_token()
        else:
            UwU.next_token()

    def report_error(UwU, message):
        if UwU.current_token:
            _, _, start_pos, end_pos = UwU.current_token
            error = {
                'message': message,
                'token': UwU.current_token,
                'position': start_pos,
                'length': end_pos - start_pos
            }
            UwU.errors.append(error)
        else:
            error = {
                'message': message,
                'token': None,
                'position': UwU.position,
                'length': 1
            }
            UwU.errors.append(error)
        # Advance to prevent infinite loops
        UwU.next_token()

    def skip_unexpected_tokens(UwU):
        # Skip tokens until a known good state is reached
        while UwU.current_token and UwU.current_token[0] not in ['DEDENT', 'NEWLINE', 'EOF']:
            UwU.next_token()

    def parse(UwU):
        """
        Parse the tokens into an Abstract Syntax Tree (AST).

        Returns:
            dict: The AST representing the parsed code.
        """
        while UwU.current_token is not None:
            try:
                statement = UwU.statement()
                if statement:
                    UwU.ast['statements'].append(statement)
            except Exception as e:
                UwU.report_error(f"Exception during parsing: {e}")
                UwU.next_token()  # Move to the next token
        return UwU.ast

    def statement(UwU):
        if UwU.current_token is None:
            return None

        token_type = UwU.current_token[0]
        token_value = UwU.current_token[1]

        if token_type == 'IDENTIFIER':
            if token_value in ['baka', 'nuu', 'kawaii', 'nyan']:
                return UwU.variable_declaration()
            elif token_value in ['dewf', 'pwease']:
                return UwU.function_definition()
            elif token_value == 'ifflie':
                return UwU.if_statement()
            elif token_value == 'whiwile':
                return UwU.while_statement()
            elif token_value == 'impowt':
                return UwU.import_statement()
            elif token_value == 'wetuwn':
                return UwU.return_statement()
            else:
                # Handle assignments or function calls
                return UwU.assignment_or_function_call()
        else:
            UwU.report_error(f"Unexpected token '{token_value}'")
            # Skip to the next statement
            UwU.skip_to_next_statement()
            return None

    def variable_declaration(UwU):
        """
        Parse a variable declaration with a type.

        Returns:
            dict: The AST node representing the variable declaration.
        """
        var_type = UwU.current_token[1]
        UwU.eat('IDENTIFIER')  # Consume type keyword

        if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER':
            variable_name = UwU.current_token[1]
            UwU.eat('IDENTIFIER')  # Consume variable name

            if UwU.current_token_is('OPERATOR', '='):
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
        """
        Parse an import statement.

        Returns:
            dict: The AST node representing the import statement.
        """
        UwU.eat('IDENTIFIER', 'impowt')  # Consume 'impowt'

        if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER':
            module_name = UwU.current_token[1]
            UwU.eat('IDENTIFIER')  # Consume the module name
            return {'type': 'import', 'module': module_name}
        else:
            UwU.report_error(f"Expected module name after 'impowt', but got {UwU.current_token[0] if UwU.current_token else 'EOF'}")
            return None

    def function_definition(UwU):
        try:
            logging.debug("Entering function_definition")
            if UwU.current_token and UwU.current_token[1] in ['dewf', 'pwease']:
                UwU.eat('IDENTIFIER')  # Consume 'dewf' or 'pwease'
            else:
                UwU.report_error(f"Expected function definition keyword 'dewf' or 'pwease', but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                UwU.next_token()
                return None

            # Expect function name
            if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER':
                function_name = UwU.current_token[1]
                UwU.eat('IDENTIFIER')
            else:
                UwU.report_error(f"Expected function name after 'pwease', but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                UwU.next_token()
                return None

            # Expect '('
            if UwU.current_token_is('SYMBOL', '('):
                UwU.eat('SYMBOL', '(')
            else:
                UwU.report_error(f"Expected '(' after function name, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                UwU.next_token()
                return None

            parameters = []
            while UwU.current_token and not UwU.current_token_is('SYMBOL', ')'):
                if UwU.current_token[0] == 'IDENTIFIER':
                    param_type = UwU.current_token[1]
                    UwU.eat('IDENTIFIER')  # Consume parameter type

                    if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER':
                        param_name = UwU.current_token[1]
                        UwU.eat('IDENTIFIER')  # Consume parameter name
                    else:
                        UwU.report_error(f"Expected parameter name after type, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                        UwU.next_token()
                        return None

                    if UwU.current_token_is('OPERATOR', '='):
                        UwU.eat('OPERATOR', '=')
                        default_value = UwU.expression()
                        parameters.append({'type': param_type, 'name': param_name, 'default': default_value})
                    else:
                        parameters.append({'type': param_type, 'name': param_name})

                    if UwU.current_token_is('SYMBOL', ','):
                        UwU.eat('SYMBOL', ',')  # Consume commas between parameters
                    elif not UwU.current_token_is('SYMBOL', ')'):
                        UwU.report_error(f"Expected ',' or ')' in parameter list, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                        UwU.next_token()
                else:
                    UwU.report_error(f"Expected parameter type, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                    UwU.next_token()

            # Expect ')'
            if UwU.current_token_is('SYMBOL', ')'):
                UwU.eat('SYMBOL', ')')
            else:
                UwU.report_error(f"Expected ')' at the end of parameter list, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                UwU.next_token()
                return None

            # Expect ':'
            if UwU.current_token_is('SYMBOL', ':'):
                UwU.eat('SYMBOL', ':')
            else:
                UwU.report_error(f"Expected ':' after parameter list, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
                # For robustness, you might choose to skip to the next statement
                UwU.skip_to_next_statement()

            # Parse function body
            body = UwU.block()
            logging.debug("Exiting function_definition")

            return {'type': 'function_definition', 'name': function_name, 'parameters': parameters, 'body': body}
        except Exception as e:
            UwU.report_error(f"Exception during function definition parsing: {e}")
            UwU.next_token()
            return None

    def block(UwU):
        statements = []

        # Expect an 'INDENT' token to start a block
        if UwU.current_token and UwU.current_token[0] == 'INDENT':
            UwU.eat('INDENT')
        else:
            UwU.report_error("Expected INDENT to start a block.")
            UwU.skip_to_block_end()
            return statements  # Return empty block

        # Parse statements until 'DEDENT' is encountered
        while UwU.current_token and UwU.current_token[0] != 'DEDENT':
            stmt = UwU.statement()
            if stmt:
                statements.append(stmt)
            else:
                # Advance to prevent infinite loops
                UwU.next_token()

        # Consume the 'DEDENT' token
        if UwU.current_token and UwU.current_token[0] == 'DEDENT':
            UwU.eat('DEDENT')
        else:
            UwU.report_error("Expected DEDENT to end the block.")
            UwU.next_token()

        return statements

    def return_statement(UwU):
        """
        Parse a return statement.

        Returns:
            dict: The AST node representing the return statement.
        """
        UwU.eat('IDENTIFIER', 'wetuwn')  # Consume 'wetuwn'
        value = UwU.expression()  # Parse the expression to return
        return {'type': 'return', 'value': value}

    def assignment_or_function_call(UwU):
        if UwU.current_token is None:
            UwU.report_error("Expected identifier, but got EOF")
            return None

        token_type, token_value, _, _ = UwU.current_token
        if token_type != 'IDENTIFIER':
            UwU.report_error(f"Expected identifier, but got {token_type}")
            return None

        identifier = token_value
        UwU.eat('IDENTIFIER')  # Consume the identifier

        # Handle assignment
        if UwU.current_token_is('OPERATOR', '='):
            UwU.eat('OPERATOR', '=')  # Consume '='
            value = UwU.expression()  # Parse the expression on the right-hand side
            return {'type': 'assignment', 'variable': identifier, 'value': value}

        # Handle function call
        elif UwU.current_token_is('SYMBOL', '('):
            UwU.eat('SYMBOL', '(')  # Consume '('
            args = []

            # Parse function arguments until we encounter ')'
            while UwU.current_token and not UwU.current_token_is('SYMBOL', ')'):
                arg = UwU.expression()
                if arg:
                    args.append(arg)
                if UwU.current_token_is('SYMBOL', ','):
                    UwU.eat('SYMBOL', ',')  # Consume commas between arguments
                elif not UwU.current_token_is('SYMBOL', ')'):
                    UwU.report_error(f"Expected ',' or ')' in argument list, but got {UwU.current_token[1]}")
                    UwU.next_token()
            UwU.eat('SYMBOL', ')')  # Consume closing ')'

            return {'type': 'function_call', 'name': identifier, 'arguments': args}

        else:
            UwU.report_error(f"Expected '=' or '(' after identifier, but got '{UwU.current_token[1] if UwU.current_token else 'EOF'}'")
            UwU.next_token()
            return None

    def if_statement(UwU):
        """
        Parse an if statement.

        Returns:
            dict: The AST node representing the if statement.
        """
        UwU.eat('IDENTIFIER', 'ifflie')  # Consume 'ifflie'
        condition = UwU.expression()  # Parse the condition expression
        UwU.eat('SYMBOL', ':')  # Expect ':'

        # Parse the if block
        if_body = UwU.block()

        # Check for 'elswe' clause
        else_body = []
        if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER' and UwU.current_token[1] == 'elswe':
            UwU.eat('IDENTIFIER', 'elswe')
            UwU.eat('SYMBOL', ':')  # Expect ':'
            else_body = UwU.block()

        return {'type': 'if_statement', 'condition': condition, 'if_body': if_body, 'else_body': else_body}

    def while_statement(UwU):
        """
        Parse a while statement.

        Returns:
            dict: The AST node representing the while statement.
        """
        UwU.eat('IDENTIFIER', 'whiwile')  # Consume 'whiwile'
        condition = UwU.expression()  # Parse the condition expression
        UwU.eat('SYMBOL', ':')  # Expect ':'

        # Parse the while block
        body = UwU.block()

        return {'type': 'while_statement', 'condition': condition, 'body': body}

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
        '%': 20,
        '**': 30,
    }

    def expression(UwU, min_precedence=0):
        """
        Parse an expression with operator precedence.

        Args:
            min_precedence (int): The minimum precedence level required.

        Returns:
            dict: The AST node representing the expression.
        """
        if UwU.current_token is None:
            UwU.report_error("Unexpected end of input.")
            return None

        lhs = UwU.primary()

        while UwU.current_token and UwU.current_token[0] == 'OPERATOR' and UwU.current_token[1] in UwU.precedence and UwU.precedence[UwU.current_token[1]] >= min_precedence:
            op = UwU.current_token[1]
            op_precedence = UwU.precedence[op]
            UwU.eat('OPERATOR', op)

            rhs = UwU.expression(op_precedence + 1)
            if rhs is None:
                UwU.report_error("Right-hand side of expression is missing.")
                break
            lhs = {'type': 'binary_operation', 'operator': op, 'left': lhs, 'right': rhs}

        return lhs

    def primary(UwU):
        if UwU.current_token is None:
            UwU.report_error("Unexpected end of input.")
            return None

        token_type, token_value, _, _ = UwU.current_token

        if token_type in ['INTEGER', 'FLOAT']:
            value = token_value
            UwU.eat(token_type)
            return {'type': 'number', 'value': value}

        elif token_type == 'IDENTIFIER' and token_value in ['Twue', 'Fawlse']:
            value = token_value
            UwU.eat('IDENTIFIER')
            return {'type': 'boolean', 'value': value}

        elif token_type == 'STRING':
            value = token_value
            UwU.eat('STRING')
            return {'type': 'string', 'value': value}

        elif UwU.current_token_is('SYMBOL', '('):
            UwU.eat('SYMBOL', '(')
            expr = UwU.expression()
            UwU.eat('SYMBOL', ')')
            return expr

        elif UwU.current_token_is('SYMBOL', '['):
            UwU.eat('SYMBOL', '[')
            elements = []
            while UwU.current_token and not UwU.current_token_is('SYMBOL', ']'):
                element = UwU.expression()
                if element:
                    elements.append(element)
                if UwU.current_token_is('SYMBOL', ','):
                    UwU.eat('SYMBOL', ',')
                elif not UwU.current_token_is('SYMBOL', ']'):
                    UwU.report_error(f"Expected ',' or ']' in list, but got {UwU.current_token[1]}")
                    UwU.next_token()
            UwU.eat('SYMBOL', ']')
            return {'type': 'list', 'elements': elements}

        elif token_type == 'IDENTIFIER':
            identifier = token_value
            UwU.eat('IDENTIFIER')

            # Handle attribute access and indexing
            try:
                while True:
                    if UwU.current_token_is('SYMBOL', '.'):
                        UwU.eat('SYMBOL', '.')
                        if UwU.current_token and UwU.current_token[0] == 'IDENTIFIER':
                            attr = UwU.current_token[1]
                            UwU.eat('IDENTIFIER')
                            identifier = {'type': 'attribute_access', 'object': identifier, 'attribute': attr}
                        else:
                            UwU.report_error(f"Expected attribute name after '.', but got {UwU.current_token[1] if UwU.current_token else 'EOF'}")
                            break
                    elif UwU.current_token_is('SYMBOL', '['):
                        UwU.eat('SYMBOL', '[')
                        index = UwU.expression()
                        UwU.eat('SYMBOL', ']')
                        identifier = {'type': 'index', 'value': identifier, 'index': index}
                    else:
                        break
            except Exception as e:
                UwU.report_error(f"Error parsing identifier: {e}")
                UwU.next_token()

            # Function call
            if UwU.current_token_is('SYMBOL', '('):
                UwU.eat('SYMBOL', '(')
                args = []
                while UwU.current_token and not UwU.current_token_is('SYMBOL', ')'):
                    arg = UwU.expression()
                    if arg:
                        args.append(arg)
                    if UwU.current_token_is('SYMBOL', ','):
                        UwU.eat('SYMBOL', ',')
                    elif not UwU.current_token_is('SYMBOL', ')'):
                        UwU.report_error(f"Expected ',' or ')' in argument list, but got {UwU.current_token[1]}")
                        UwU.next_token()
                UwU.eat('SYMBOL', ')')
                return {'type': 'function_call', 'name': identifier, 'arguments': args}
            else:
                return {'type': 'identifier', 'value': identifier}
        else:
            UwU.report_error(f"Unexpected token {token_value}")
            UwU.next_token()
            return None

    # Optional: Helper function to lookup function definitions if needed
    def lookup_function_definition(UwU, function_name):
        """
        Helper function to lookup the function definition by name.

        Args:
            function_name (str): The name of the function to lookup.

        Returns:
            dict or None: The function definition AST node if found, else None.
        """
        for statement in UwU.ast['statements']:
            if statement['type'] == 'function_definition' and statement['name'] == function_name:
                return statement
        return None
    
    def skip_to_block_end(UwU):
        """
        Skip tokens until the end of the block is reached.

        This is used for error recovery when an unexpected INDENT or DEDENT is encountered.
        """
        while UwU.current_token and UwU.current_token[0] not in ['DEDENT', 'EOF']:
            UwU.next_token()

    def skip_to_next_statement(UwU):
        """
        Skip tokens until the beginning of the next statement.
        """
        while UwU.current_token and UwU.current_token[0] not in ['NEWLINE', 'DEDENT', 'INDENT', 'EOF']:
            UwU.next_token()
        # Consume the NEWLINE or DEDENT
        if UwU.current_token and UwU.current_token[0] in ['NEWLINE', 'DEDENT', 'INDENT']:
            UwU.next_token()