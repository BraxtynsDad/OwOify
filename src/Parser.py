from lexer import OwOCustomLexer
from Funny import *

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
        print(f"Advancing to token: {UwU.cuwwent_tokewn}")

    def pawse(UwU):
        try:
            UwU.ast_root = UwU.pawse_stwatement()
        except SyntaxError as e:
            UwU.handwe_ewwow(e)

    def pawse_stwatement(UwU):
        if UwU.cuwwent_tokewn is None:
            return None  # End of input or handle appropriately

        if UwU.cuwwent_tokewn[0] in KEYWORD_MAP:
            expression = UwU.pawse_expwession()
            return StatementNode(expression)
        else:
            raise SyntaxError(f"Unexpectyed token: {UwU.cuwwent_tokewn[0]}")

    def pawse_expwession(UwU):
        if UwU.cuwwent_tokewn and UwU.cuwwent_tokewn[0] in BUILTIN_MAP or UwU.cuwwent_tokewn[0].isidentifier():
            value = UwU.cuwwent_tokewn[0]
            UwU.advance()
            return ExpressionNode(value)
        else:
            raise SyntaxError(f"Invawid expwession: {UwU.cuwwent_tokewn[0]}")

    def handwe_ewwow(UwU, ewwor):
        print(f"Synwtax ewwor: {ewwor}")
        while UwU.cuwwent_tokewn and UwU.cuwwent_tokewn[0] not in KEYWORD_MAP + ["END"]:
            UwU.advance()