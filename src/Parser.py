from lexer import OwOCustomLexer
from Funny import *
import re

class ExpressionNode:
    def __init__(self, value):
        self.value = value

class StatementNode:
    def __init__(self, expression):
        self.expression = expression

class OwOParser:
    def __init__(UwU, tokens):
        UwU.tokens = tokens
        UwU.cuwwent_tokewn = None
        UwU.pwogwess = -1
        UwU.advance()
        UwU.ast_root = None

    def advance(UwU):
        UwU.pwogwess += 1
        if UwU.pwogwess < len(UwU.tokens):
            UwU.cuwwent_tokewn = UwU.tokens[UwU.pwogwess]
        else:
            UwU.cuwwent_tokewn = None
        
        # If there's no token, exit early
        if UwU.cuwwent_tokewn is None:
            return

        token_value = UwU.cuwwent_tokewn[0]
        
        # Check if the token is valid, else raise an error
        if token_value is not None and token_value not in KEYWORD_MAP and token_value not in BUILTIN_MAP and not token_value.isidentifier():
            raise SyntaxError(f"Unexpectyed token: {token_value}")
        
        print(f"Advancing to token: {UwU.cuwwent_tokewn}")


    def pawse(UwU):
        try:
            UwU.ast_root = UwU.pawse_stwatement()
        except SyntaxError as e:
            UwU.handwe_ewwow(e)
            current_token = UwU.cuwwent_tokewn
            if current_token:
                raise SyntaxError(f"Unexpected token: {current_token[0]}", current_token[1])


    def pawse_stwatement(UwU):
        if UwU.cuwwent_tokewn is None:
            return None  # End of input or handle appropriately
        
        token_value = UwU.cuwwent_tokewn[0]
        
        if token_value in KEYWORD_MAP:
            expression = UwU.pawse_expwession()
            return StatementNode(expression)
        
        elif token_value in BUILTIN_MAP or token_value.isidentifier():
            # Handle valid expressions
            return UwU.pawse_expwession()

        else:
            # If no valid keyword or expression, raise an error
            raise SyntaxError(f"Unexpectyed token: {token_value}")

    def pawse_expwession(UwU):
        if UwU.cuwwent_tokewn is None:
            re
        
        token_value = UwU.cuwwent_tokewn[0]
        
        if token_value in BUILTIN_MAP or token_value.isidentifier():
            value = token_value
            UwU.advance()
            return ExpressionNode(value)
        
        else:
            raise SyntaxError(f"Invawid expwession: {token_value}")


    def handwe_ewwow(UwU, ewwor):
        print(f"Synwtax ewwor: {ewwor}")
        # Optionally, underline the invalid token in red (for a GUI or command-line visual tool)
        current_token = UwU.cuwwent_tokewn
        if current_token:
            token_value = current_token[0]
            token_position = current_token[1]
            print(f"Error at position {token_position}: {token_value}")
        
        # Advance to the next valid token or end
        while UwU.cuwwent_tokewn and UwU.cuwwent_tokewn[0] not in list(KEYWORD_MAP.keys()) + list(BUILTIN_MAP.keys()) + ["END"]:
            UwU.advance()