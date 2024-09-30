# lexer.py

import re
from PyQt5.QtGui import QColor
from PyQt5.Qsci import QsciLexerCustom
from Funny import combined_map  # Assuming this contains your keyword mappings

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
        UwU.setColor(QColor("#FF1493"), UwU.FUNCTIONSIES)   # Deep Pink
        UwU.setColor(QColor("#1E90FF"), UwU.CWASSES)        # Dodger Blue
        UwU.setColor(QColor("#7FFF00"), UwU.FUNCTION_DEWF)  # Chartreuse

        UwU.tOwOkens_list = []

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
        """Tokenizes the text and stores the tokens, including indentation."""
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
            indent_str = indent_str.replace('\t', '    ')  # Convert tabs to 4 spaces
            indent_level = len(indent_str)
            stripped_line = line[len(indent_str):]
            line_start_pos = pos
            indent_end_pos = line_start_pos + len(indent_str)

            if indent_level > indentation_stack[-1]:
                indentation_stack.append(indent_level)
                tokens.append(('INDENT', '', line_start_pos, indent_end_pos))
            elif indent_level < indentation_stack[-1]:
                while indentation_stack and indent_level < indentation_stack[-1]:
                    indentation_stack.pop()
                    tokens.append(('DEDENT', '', line_start_pos, indent_end_pos))

            line_pos = pos + len(indent_str)
            for match in p.finditer(stripped_line):
                token_type = match.lastgroup
                token_value = match.group()
                token_start = line_pos + match.start()
                token_end = line_pos + match.end()

                if token_type == 'WHITESPACE' or token_type == 'NEWLINE':
                    # Skip whitespace and newline tokens within a line
                    continue
                elif token_type == 'UNKNOWN':
                    # Optionally, report or handle unknown tokens
                    # For now, skip unknown tokens
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

    def tokenize_for_highlighting(UwU, text):
        """Tokenizes the text for syntax highlighting, without indentation tokens."""
        # Normalize line endings to \n
        text = text.replace('\r\n', '\n').replace('\r', '\n')

        p = re.compile(
            r'''
            (?P<COMMENT>x3[^\n]*)                   # Comment starting with x3
            | (?P<STRING>"[^"\n]*"|'[^'\n]*')       # String literals
            | (?P<OPERATOR>==|!=|<=|>=|[+\-*/%<>=]) # Operators
            | (?P<FLOAT>
                (?:\d+\.\d*|\.\d+)
                (?:[eE][+-]?\d+)?
            )                                       # Floating-point numbers
            | (?P<INTEGER>\d+(?:[eE][+-]?\d+)?)     # Integers and numbers with exponents
            | (?P<IDENTIFIER>\w+)                   # Identifiers
            | (?P<SYMBOL>[()\[\]{},.:])             # Symbols
            | (?P<WHITESPACE>[ \t]+)                # Whitespace
            | (?P<NEWLINE>\n)                       # Newline
            | (?P<UNKNOWN>.)                        # Any other character
            ''',
            re.VERBOSE
        )

        tokens = []
        for match in p.finditer(text):
            token_type = match.lastgroup
            token_value = match.group()
            token_start = match.start()
            token_end = match.end()

            if token_type == 'UNKNOWN':
                # Skip unknown tokens
                continue
            else:
                tokens.append((token_type, token_value, token_start, token_end))

        return tokens

    def styleText(UwU, start: int, end: int) -> None:
        UwU.startStyling(start)
        text = UwU.editor.text()

        tokens = UwU.tokenize_for_highlighting(text)

        # Find the index of the first token to style
        token_index = 0
        while token_index < len(tokens) and tokens[token_index][2] < start:
            token_index += 1

        while token_index < len(tokens):
            token_type, token_value, token_start, token_end = tokens[token_index]
            if token_start >= end:
                break

            # Calculate the length of the token within the styling range
            token_length = token_end - token_start
            if token_length <= 0:
                token_index += 1
                continue  # Skip tokens with zero length

            # Determine the style based on token_type
            if token_type == 'COMMENT':
                style = UwU.COMMWENTS
            elif token_type == 'IDENTIFIER':
                if token_value in combined_map:
                    style = UwU.KEYYWOwOWD
                else:
                    style = UwU.DEWFULT
            elif token_type in ['INTEGER', 'FLOAT']:
                style = UwU.CONSTAWNTS
            elif token_type == 'STRING':
                style = UwU.STWING
            elif token_type == 'SYMBOL':
                style = UwU.BWACKETS
            elif token_type == 'OPERATOR':
                style = UwU.TYPESIES
            else:
                style = UwU.DEWFULT

            # Apply styling
            UwU.setStyling(token_length, style)
            token_index += 1