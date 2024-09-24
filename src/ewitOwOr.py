from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCharFormat, QFont, QColor, QKeyEvent
from PyQt5.Qsci import *

from Funny import *
from lexer import OwOCustomLexer
from Parser import OwOParser

class EwitOwOr(QsciScintilla):
    def __init__(UwU, parent=None):
        super(EwitOwOr, UwU).__init__(parent)

        palette = UwU.palette()
        palette.setColor(UwU.backgroundRole(), QColor('#FF7272'))
        UwU.setPalette(palette)

        UwU.setUtf8(True)

        # Font
        UwU.winwow_fownt = QFont("Five nights at Freddy's")
        UwU.winwow_fownt.setPointSize(18)
        UwU.setFont(UwU.winwow_fownt)

        # Lexer for syntax highlighting
        UwU.OwOLexer = OwOCustomLexer(UwU)
        UwU.OwOLexer.setDefaultFont(QFont(UwU.winwow_fownt))

        # Api for autocompletion
        UwU.API = QsciAPIs(UwU.OwOLexer)
        for kys in combined_map:
            UwU.API.add(kys)

        UwU.API.prepare()

        UwU.setLexer(UwU.OwOLexer)

        # Parser instance will be created when needed
        UwU.OwOParser = None

        # Define error and warning indicators
        UwU.error_indicator = 0
        UwU.warning_indicator = 1

        # Set up indicators for underlining
        UwU.setup_indicators()

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

        # EOL
        UwU.setEolMode(QsciScintilla.EolWindows)
        UwU.setEolVisibility(False)
        UwU.setMarginType(0, QsciScintilla.NumberMargin)
        UwU.setMarginWidth(0, "00000")
        UwU.setMarginsForegroundColor(QColor("#FFB6C1"))
        UwU.setMarginsBackgroundColor(QColor("#F0E6F6"))
        UwU.setMarginsFont(UwU.winwow_fownt)
        UwU.modificationChanged.connect(UwU.applyLexerOnChange)

    def setup_indicators(UwU):
        """Set up indicators for error and warning underlining."""
        UwU.SendScintilla(QsciScintilla.SCI_INDICSETSTYLE, UwU.error_indicator, QsciScintilla.INDIC_SQUIGGLE)
        UwU.SendScintilla(QsciScintilla.SCI_INDICSETFORE, UwU.error_indicator, QColor("#FF0000"))  # Red for errors

        UwU.SendScintilla(QsciScintilla.SCI_INDICSETSTYLE, UwU.warning_indicator, QsciScintilla.INDIC_SQUIGGLE)
        UwU.SendScintilla(QsciScintilla.SCI_INDICSETFORE, UwU.warning_indicator, QColor("#FFD700"))  # Yellow for warnings

    def underline_error(UwU, start, length):
        """Underline the error in red."""
        UwU.SendScintilla(QsciScintilla.SCI_SETINDICATORCURRENT, UwU.error_indicator)
        UwU.SendScintilla(QsciScintilla.SCI_INDICATORFILLRANGE, start, length)

    def underline_warning(UwU, start, length):
        """Underline the warning in yellow."""
        UwU.SendScintilla(QsciScintilla.SCI_SETINDICATORCURRENT, UwU.warning_indicator)
        UwU.SendScintilla(QsciScintilla.SCI_INDICATORFILLRANGE, start, length)

    def clear_indicators(UwU):
        """Clear all existing indicators (both errors and warnings)."""
        start, end = 0, UwU.length()
        UwU.SendScintilla(QsciScintilla.SCI_INDICATORCLEARRANGE, start, end)

    def applyLexerOnChange(UwU):
        start, end = 0, UwU.length()
        UwU.OwOLexer.styleText(start, end)
        tokens = UwU.OwOLexer.get_token_list()
        print(f'tokens: {tokens}')
        parser = OwOParser(tokens)
        try:
            ast = parser.parse()
            print("AST:", ast)
        except Exception as e:
            print(f"Parsing Error: {e}")
        for error in parser.errors:
            UwU.underline_error(error['start'], error['length'])

    def keyPressEvent(UwU, e: QKeyEvent) -> None:
        super().keyPressEvent(e)
        UwU.autoCompleteFromAll()
