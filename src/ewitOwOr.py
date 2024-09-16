from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

from Funny import *
import pkgutil
from lexer import OwOCustomLexer
from Parser import OwOParser

class EwitOwOr(QsciScintilla):

    def __init__(UwU, parent=None):
        super(EwitOwOr, UwU).__init__(parent)

        palette = UwU.palette()
        palette.setColor(UwU.backgroundRole(), QColor('#FF7272'))
        UwU.setPalette(palette)
        # UTF-8 is a character encoding standard that is used to encode all characters in the Unicode character set
        # The goal of Unicode is to provide a consistent way to encode multilingual text
        UwU.setUtf8(True)
        # Font
        UwU.winwow_fownt = QFont("Five Nights at Freddy's")
        UwU.winwow_fownt.setPointSize(18)
        UwU.setFont(UwU.winwow_fownt)

        # Lexer for syntax highlighting 
        UwU.OwOLexer = OwOCustomLexer(UwU)
        UwU.OwOLexer.setDefaultFont(QFont(UwU.winwow_fownt))

        # Api (you can add autocompletion using this)
        UwU.API = QsciAPIs(UwU.OwOLexer)
        for kys in combined_map:
            UwU.API.add(kys)

        UwU.API.prepare()

        UwU.setLexer(UwU.OwOLexer)

        # Parser instance will be created when needed
        UwU.OwOParser = None

        # Brace Matching
        UwU.setBraceMatching(QsciScintilla.SloppyBraceMatch)
  
        # Indentation
        UwU.setIndentationGuides(True)
        UwU.setTabWidth(4)
        UwU.setIndentationsUseTabs(False)
        UwU.setAutoIndent(True)
        # Autocomplete
        UwU.setAutoCompletionSource(QsciScintilla.AcsAPIs)  # Use APIs only
        UwU.setAutoCompletionThreshold(1) # autocomplete will show after one character
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
        # Line Numbers
        UwU.setMarginType(0, QsciScintilla.NumberMargin)
        UwU.setMarginWidth(0, "00000")
        UwU.setMarginsForegroundColor(QColor("#FFB6C1"))  # Light pastel pink
        UwU.setMarginsBackgroundColor(QColor("#F0E6F6"))  # Light pastel lavender
        UwU.setMarginsFont(UwU.winwow_fownt)
        # UwU.keyPressEvent = UwU.hARAndwe_ewitOwOr_pwess

    def keyPressEvent(UwU, e: QKeyEvent) -> None:
        texty = UwU.text()
        stawat = 0 
        endx3 = len(texty)
        towoken_list = UwU.OwOLexer.get_tOwOkens(stawat, endx3)
        UwU.OwOParser = OwOParser(towoken_list)
        UwU.OwOParser.pawse()
        UwU.autoCompleteFromAll()
        return super().keyPressEvent(e)