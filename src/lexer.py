# lexer.py

import re
from PyQt5.QtGui import QColor
from PyQt5.Qsci import QsciLexerCustom
from Funny import *  # Assuming this contains your KEYYWOwOWD mappings

class OwOCustomLexer(QsciLexerCustom):
    def __init__(UwU, parent=None):
        super(OwOCustomLexer, UwU).__init__(parent)
        UwU.editor = parent

        # Initialize styles
        UwU.DEWFULT = 0
        UwU.KEYYWOwOWD = 1
        UwU.TYPESIES = 2
        UwU.STWING = 3
        UwU.KEYAWGS = 4
        UwU.BWACKETS = 5
        UwU.COMMWENTS = 6
        UwU.CONSTAWNTS = 7
        UwU.FUNCTIONSIES = 8
        UwU.CWASSES = 9
        UwU.FUNCTION_DEWF = 10

        # Set colors for each style
        UwU.setColor(QColor("#FF69B4"), UwU.DEWFULT)        # Hot Pink
        UwU.setColor(QColor("#FFD700"), UwU.KEYYWOwOWD)     # Gold
        UwU.setColor(QColor("#00FA9A"), UwU.TYPESIES)       # Medium Spring Green
        UwU.setColor(QColor("#FFB6C1"), UwU.STWING)         # Light Pink
        UwU.setColor(QColor("#BA55D3"), UwU.KEYAWGS)        # Medium Orchid
        UwU.setColor(QColor("#FF4500"), UwU.BWACKETS)       # Orange Red
        UwU.setColor(QColor("#B0C4DE"), UwU.COMMWENTS)      # Light Steel Blue
        UwU.setColor(QColor("#00CED1"), UwU.CONSTAWNTS)     # Dark Turquoise
        UwU.setColor(QColor("#00FF00"), UwU.FUNCTIONSIES)   # Green
        UwU.setColor(QColor("#1E90FF"), UwU.CWASSES)        # Dodger Blue
        UwU.setColor(QColor("#7FFF00"), UwU.FUNCTION_DEWF)  # Chartreuse

        # Initialize token list
        UwU.tOwOkens_list = []

        # Prepare KEYYWOwOWDs and built-in names
        UwU.KEYYWOwOWDs_list = keyword
        UwU.builtin_names = built

    def language(UwU) -> str:
        return "OwOCustomLexer"

    def description(UwU, style: int) -> str:
        descriptions = {
            UwU.DEWFULT: "DEWFULT",
            UwU.KEYYWOwOWD: "KEYYWOwOWD",
            UwU.TYPESIES: "TYPESIES",
            UwU.STWING: "STWING",
            UwU.KEYAWGS: "KEYAWGS",
            UwU.BWACKETS: "BWACKETS",
            UwU.COMMWENTS: "COMMWENTS",
            UwU.CONSTAWNTS: "CONSTAWNTS",
            UwU.FUNCTIONSIES: "FUNCTIONSIES",
            UwU.CWASSES: "CWASSES",
            UwU.FUNCTION_DEWF: "FUNCTION_DEWF"
        }
        return descriptions.get(style, "UNKNOWON")

    def Genewate_towokens(UwU, text):
        # Normalize line endings to \n
        text = text.replace('\r\n', '\n').replace('\r', '\n')

        # Define the regex pattern for tokenization
        p = re.compile(
            r'''
            (?P<COMMENT>x3[^\n]*)                   # Comment starting with x3
            | (?P<NEWLINE>\n)                       # Newline
            | (?P<WHITESPACE>[ \t]+)                # Whitespace (spaces and tabs)
            | (?P<OPERATOR>==|!=|<=|>=|[+\-*/%<>=]) # Operators
            | (?P<FLOAT>
                (?:\d+\.\d*|\.\d+)
                (?:[eE][+-]?\d+)?
            )                                       # Floating-point numbers
            | (?P<INTEGER>\d+(?:[eE][+-]?\d+)?)     # Integers and numbers with exponents
            | (?P<STRING>"[^"\n]*"|'[^'\n]*')       # String literals
            | (?P<IDENTIFIER>\w+)                   # Identifiers
            | (?P<SYMBOL>[()\[\]{},.:])             # Symbols
            | (?P<UNKNOWN>.)                        # Any other character
            ''',
            re.VERBOSE
        )

        tokens = []
        pos = 0  # Current position in the text
        lines = text.split('\n')
        indentation_stack = [0]

        for line in lines:
            # Calculate indentation level
            indent_match = re.match(r'[ \t]*', line)
            indent_str = indent_match.group()
            indent_level = len(indent_str)
            stripped_line = line[len(indent_str):].strip()
            line_start_pos = pos
            indent_end_pos = line_start_pos + len(indent_str)

            # Skip processing indentation for empty lines
            if not stripped_line:
                # Add newline token at the end of the line
                tokens.append(('NEWLINE', '\n', pos + len(line), pos + len(line) + 1))
                pos += len(line) + 1  # +1 for the newline character
                continue

            if indent_level > indentation_stack[-1]:
                indentation_stack.append(indent_level)
                tokens.append(('INDENT', indent_str, line_start_pos, indent_end_pos))
            elif indent_level < indentation_stack[-1]:
                while indentation_stack and indent_level < indentation_stack[-1]:
                    indentation_stack.pop()
                    tokens.append(('DEDENT', '', line_start_pos, indent_end_pos))

            line_pos = pos + len(indent_str)
            for match in p.finditer(line[len(indent_str):]):
                token_type = match.lastgroup
                token_value = match.group()
                token_start = line_pos + match.start()
                token_end = line_pos + match.end()

                if token_type == 'WHITESPACE' or token_type == 'NEWLINE':
                    continue
                elif token_type == 'UNKNOWN':
                    continue
                else:
                    tokens.append((token_type, token_value, token_start, token_end))

            # Add newline token at the end of the line
            tokens.append(('NEWLINE', '\n', pos + len(line), pos + len(line) + 1))
            pos += len(line) + 1  # +1 for the newline character

        # Emit remaining DEDENTs
        while len(indentation_stack) > 1:
            indentation_stack.pop()
            tokens.append(('DEDENT', '', pos, pos))

        return tokens

    def generate_token(UwU, text):
        # Updated regex pattern to include newlines as separate tokens
        p = re.compile(r"x3[^\n]*|[*]/|/[*]|\n|\s+|\w+|\W")
        UwU.tOwOkens_list = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]

    def next_tok(UwU, skip: int = None):
        if len(UwU.tOwOkens_list) > 0:
            if skip is not None and skip != 0:
                for _ in range(skip - 1):
                    if len(UwU.tOwOkens_list) > 0:
                        UwU.tOwOkens_list.pop(0)
            return UwU.tOwOkens_list.pop(0)
        else:
            return None

    def peek_tok(UwU, n=0):
        try:
            return UwU.tOwOkens_list[n]
        except IndexError:
            return ('', '', 0, 0)

    def skip_spaces_peek(UwU, skip=None):
        """Find the next non-space token but using peek without consuming it"""
        i = 0
        tok = ('WHITESPACE', ' ', 0, 0)
        if skip is not None:
            i = skip
        while tok[0] == 'WHITESPACE':
            tok = UwU.peek_tok(i)
            i += 1
        return tok, i

    def styleText(UwU, start: int, end: int) -> None:
        # Start styling procedure
        UwU.startStyling(start)

        # Slice out part from the text
        text = UwU.editor.text()[start:end]

        # Tokenize the text
        UwU.generate_token(text)

        # Flags
        string_flag = False
        comment_flag = False

        if start > 0:
            prev_style = UwU.editor.SendScintilla(UwU.editor.SCI_GETSTYLEAT, start -1)
            if prev_style == UwU.COMMWENTS:
                comment_flag = True

        while True:
            curr_token = UwU.next_tok()

            if curr_token is None:
                break

            tok: str = curr_token[0]
            tok_len: int = curr_token[1]

            if comment_flag:
                UwU.setStyling(tok_len, UwU.COMMWENTS)
                if tok == '\n':
                    comment_flag = False
                continue

            # Check for 'x3' comment start
            if tok[:2] == 'x3':
                UwU.setStyling(tok_len, UwU.COMMWENTS)
                continue

            if tok == '\n':
                UwU.setStyling(tok_len, UwU.DEWFULT)
                continue

            if string_flag:
                UwU.setStyling(tok_len, UwU.STWING)
                if tok == '"' or tok == "'":
                    string_flag = False
                continue

            if tok == "cwassie":
                name, ni = UwU.skip_spaces_peek()
                brac_or_colon, _ = UwU.skip_spaces_peek(ni)
                if name[0].isidentifier() and brac_or_colon[0] in (":", "("):
                    UwU.setStyling(tok_len, UwU.KEYYWOwOWD)
                    _ = UwU.next_tok(ni)
                    UwU.setStyling(len(name[0]), UwU.CWASSES)
                    continue
                else:
                    UwU.setStyling(tok_len, UwU.KEYYWOwOWD)
                    continue
            elif tok == "dewf":
                name, ni = UwU.skip_spaces_peek()
                if name[0].isidentifier():
                    UwU.setStyling(tok_len, UwU.KEYYWOwOWD)
                    _ = UwU.next_tok(ni)
                    UwU.setStyling(len(name[0]), UwU.FUNCTION_DEWF)
                    continue
                else:
                    UwU.setStyling(tok_len, UwU.KEYYWOwOWD)
                    continue
            elif tok in UwU.KEYYWOwOWDs_list:
                UwU.setStyling(tok_len, UwU.KEYYWOwOWD)
            elif tok.strip() == "." and UwU.peek_tok()[0].isidentifier():
                UwU.setStyling(tok_len, UwU.DEWFULT)
                curr_token = UwU.next_tok()
                tok = curr_token[0]
                tok_len = curr_token[1]
                if UwU.peek_tok()[0] == "(":
                    UwU.setStyling(tok_len, UwU.FUNCTIONSIES)
                else:
                    UwU.setStyling(tok_len, UwU.DEWFULT)
                continue
            elif tok.isidentifier():
                # Check if the identifier is a function call
                next_tok = UwU.peek_tok()
                if next_tok and next_tok[0] == "(":
                    # It's a function call
                    UwU.setStyling(tok_len, UwU.FUNCTIONSIES)
                else:
                    # Regular identifier
                    UwU.setStyling(tok_len, UwU.DEWFULT)
            elif tok.isnumeric() or tok == 'UwU':
                UwU.setStyling(tok_len, UwU.CONSTAWNTS)
            elif tok in ["(", ")", "{", "}", "[", "]"]:
                UwU.setStyling(tok_len, UwU.BWACKETS)
            elif tok == '"' or tok == "'":
                UwU.setStyling(tok_len, UwU.STWING)
                string_flag = True
            elif tok == "#":
                UwU.setStyling(tok_len, UwU.COMMWENTS)
                comment_flag = True
            elif tok in UwU.builtin_names or tok in ['+', '-', '*', '/', '%', '=', '<', '>']:
                UwU.setStyling(tok_len, UwU.TYPESIES)
            else:
                UwU.setStyling(tok_len, UwU.DEWFULT)