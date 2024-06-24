from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtWidgets import QWidget
import keyword
import pkgutil

class EwitOwOr(QsciScintilla):

    def __init__(UwU, parent=None):
        super(EwitOwOr, UwU).__init__(parent)

        # UTF-8 is a character encoding standard that is used to encode all characters in the Unicode character set
        # The goal of Unicode is to provide a consistent way to encode multilingual text
        UwU.setUtf8(True)
        # Font
        UwU.winwow_fownt = QFont("Five Nights at Freddy's")
        UwU.winwow_fownt.setPointSize(18)
        UwU.setFont(UwU.winwow_fownt)

        # Brace Matching
        UwU.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Indentation
        UwU.setIndentationGuides(True)
        UwU.setTabWidth(4)
        UwU.setIndentationsUseTabs(False)
        UwU.setAutoIndent(True)

        # Autocomplete
        UwU.setAutoCompletionSource(QsciScintilla.AcsAll)
        UwU.setAutoCompletionThreshold(1) # autocomplete will show after one character
        UwU.setAutoCompletionCaseSensitivity(False)
        UwU.setAutoCompletionUseSingle(QsciScintilla.AcusNever)

        # Caret
        UwU.setCaretForegroundColor(QColor("#C724B1"))
        UwU.setCaretLineVisible(True)
        UwU.setCaretLineBackgroundColor(QColor("#FFBCD9"))
        UwU.setCaretWidth(1)

        # EOL
        UwU.setEolMode(QsciScintilla.EolWindows)
        UwU.setEolVisibility(False)

        # Lexer for syntax highlighting 
        UwU.pylexer = QsciLexerPython()
        UwU.pylexer.setFont(QFont(UwU.winwow_fownt))
        UwU.pylexer.setDefaultFont(QFont(UwU.winwow_fownt))

        # Api (you can add autocompletion using this)
        UwU.API = QsciAPIs(UwU.pylexer)
        for kys in keyword.kwlist + dir(__builtins__):
            UwU.API.add(kys)

        for _, name, _ in pkgutil.iter_modules():
            UwU.API.add(name)

        # for future refrence
        # you can add custom function with its parametars and QSciScintilla will handle it for example
        UwU.API.add("additon(a: int, b: int)")

        UwU.API.prepare()

        UwU.setLexer(UwU.pylexer)

        # Line Numbers
        UwU.setMarginType(0, QsciScintilla.NumberMargin)
        UwU.setMarginWidth(0, "00000")
        UwU.setMarginsForegroundColor(QColor("#FFB6C1"))  # Light pastel pink
        UwU.setMarginsBackgroundColor(QColor("#F0E6F6"))  # Light pastel lavender

        UwU.setMarginsFont(UwU.winwow_fownt)

        # UwU.keyPressEvent = UwU.hARAndwe_ewitOwOr_pwess

    def keyPressEvent(UwU, e: QKeyEvent) -> None:
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Space:
            UwU.autoCompleteFromAll()
        else:
            return super().keyPressEvent(e)