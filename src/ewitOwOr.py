# editor.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCharFormat, QFont, QColor, QKeyEvent
from PyQt5.Qsci import *

from Funny import combined_map  # Assuming combined_map is defined in Funny.py
from lexer import OwOCustomLexer
from Parser import OwOParser

class EwitOwOr(QsciScintilla):
    def __init__(UwU, parent=None, file_extension=None):
        super(EwitOwOr, UwU).__init__(parent)
        UwU.file_extension = file_extension

        # Set the background color
        palette = UwU.palette()
        palette.setColor(UwU.backgroundRole(), QColor('#FF7272'))
        UwU.setPalette(palette)

        UwU.setUtf8(True)

        # Font
        UwU.winwow_fownt = QFont("Five nights at Freddy's", 18)
        UwU.setFont(UwU.winwow_fownt)
        UwU.setMarginsFont(UwU.winwow_fownt)

        # Lexer for syntax highlighting
        UwU.OwOLexer = OwOCustomLexer(UwU)
        UwU.OwOLexer.setFont(UwU.winwow_fownt)
        UwU.setLexer(UwU.OwOLexer)

        # API for autocompletion
        UwU.API = QsciAPIs(UwU.OwOLexer)
        for kys in combined_map:
            UwU.API.add(kys)
        UwU.API.prepare()

        # Parser instance will be created when needed
        UwU.OwOParser = None

        # Initialize indicators for errors
        # Background highlight indicator
        UwU.ERROR_INDICATOR_BG = 0
        UwU.indicatorDefine(QsciScintilla.INDIC_FULLBOX, UwU.ERROR_INDICATOR_BG)
        UwU.setIndicatorForegroundColor(QColor("#FFCCCC"), UwU.ERROR_INDICATOR_BG)
        # Use SendScintilla to set alpha
        UwU.SendScintilla(QsciScintilla.SCI_INDICSETALPHA, UwU.ERROR_INDICATOR_BG, 150)
        UwU.setIndicatorDrawUnder(False, UwU.ERROR_INDICATOR_BG)

        # Text color change indicator
        UwU.ERROR_INDICATOR_FG = 1
        UwU.indicatorDefine(QsciScintilla.INDIC_TEXTFORE, UwU.ERROR_INDICATOR_FG)
        UwU.setIndicatorForegroundColor(QColor("#FF0000"), UwU.ERROR_INDICATOR_FG)

        # Enable mouse tracking and call tips for hover functionality
        UwU.setMouseTracking(True)
        UwU.setCallTipsVisible(True)
        UwU.setCallTipsStyle(QsciScintilla.CallTipsNoContext)
        UwU.setCallTipsBackgroundColor(QColor("#FFFFE0"))  # Light yellow background
        UwU.setCallTipsForegroundColor(QColor("#000000"))  # Black text

        # Initialize parser errors storage
        UwU.parser_errors = []

        # Brace Matching
        UwU.setBraceMatching(QsciScintilla.SloppyBraceMatch)
  
        # Indentation
        UwU.setIndentationGuides(True)
        UwU.setTabWidth(4)
        UwU.setIndentationsUseTabs(False)
        UwU.setAutoIndent(True)

        # Autocomplete
        UwU.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        UwU.setAutoCompletionThreshold(1)
        UwU.setAutoCompletionCaseSensitivity(False)
        UwU.setAutoCompletionUseSingle(QsciScintilla.AcusNever)

        # Caret
        UwU.setCaretForegroundColor(QColor("#C724B1"))
        UwU.setCaretLineVisible(True)
        UwU.setCaretLineBackgroundColor(QColor("#E6E6FA"))
        UwU.setCaretWidth(1)

        # Margins
        UwU.setMarginType(0, QsciScintilla.NumberMargin)
        UwU.setMarginWidth(0, "00000")
        UwU.setMarginsForegroundColor(QColor("#FFB6C1"))
        UwU.setMarginsBackgroundColor(QColor("#F0E6F6"))
        UwU.setMarginsFont(UwU.winwow_fownt)

        # Connect the textChanged signal to update the lexer and parse the code
        UwU.textChanged.connect(UwU.applyLexerOnChange)

    def clear_indicators(UwU):
        length = UwU.length()
        for indicator in [UwU.ERROR_INDICATOR_BG, UwU.ERROR_INDICATOR_FG]:
            UwU.SendScintilla(QsciScintilla.SCI_SETINDICATORCURRENT, indicator)
            UwU.SendScintilla(QsciScintilla.SCI_INDICATORCLEARRANGE, 0, length)

    def underline_error(UwU, start_pos, length):
        # Debug print to verify positions
        print(f"Underlining error at position {start_pos} with length {length}")

        # Apply background highlight
        UwU.SendScintilla(QsciScintilla.SCI_SETINDICATORCURRENT, UwU.ERROR_INDICATOR_BG)
        UwU.SendScintilla(QsciScintilla.SCI_INDICATORFILLRANGE, start_pos, length)

        # Apply red text color
        UwU.SendScintilla(QsciScintilla.SCI_SETINDICATORCURRENT, UwU.ERROR_INDICATOR_FG)
        UwU.SendScintilla(QsciScintilla.SCI_INDICATORFILLRANGE, start_pos, length)

    def applyLexerOnChange(UwU):
        text = UwU.text()
        try:
            tokens = UwU.OwOLexer.Genewate_towokens(text)
            parser = OwOParser(tokens)
            ast = parser.parse()
            print(f'AST: {ast}')
        except Exception as e:
            print(f"Unexpected Parsing Error: {e}")
            # Optionally, report the error in the editor or status bar

        # Clear existing indicators
        UwU.clear_indicators()

        # Store parser errors for hover functionality
        UwU.parser_errors = parser.errors if parser else []

        # Underline errors
        for error in UwU.parser_errors:
            start_pos = error.get('position', 0)
            length = error.get('length', 1)
            UwU.underline_error(start_pos, length)


    def keyPressEvent(UwU, e: QKeyEvent) -> None:
        super().keyPressEvent(e)
        UwU.autoCompleteFromAll()

    def indicatorEvent(UwU, pos, modifiers, event):
        if event == QsciScintilla.IndicatorMouseEvent.IndicatorMouseHover:
            # Find the error at this position
            for error in UwU.parser_errors:
                start = error['position']
                end = start + error['length']
                if start <= pos <= end:
                    # Show the call tip at the current position
                    UwU.callTipShow(pos, error['message'])
                    break
        else:
            UwU.callTipCancel()