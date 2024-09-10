from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.Qsci import * 

from pathlib import Path
from lexer import OwOCustomLexer
from autOwOcompwetew import AutOwOCompwetew
from typing import TYPE_CHECKING
from Funny import KEYYWOwOWD_WIST, bUwUiwtin_fOwOnctwions_nyans

if TYPE_CHECKING:
    from main import MainWindow

class EwitOwOr(QsciScintilla):

    def __init__(UwU, mainx3_winwow, parent=None, pathy: Path = None, is_pytOwOn_fwiwe=True):
        super(EwitOwOr, UwU).__init__(parent)

        UwU.mainx3_winwow: MainWindow = mainx3_winwow
        UwU.cuwwent_fwiwe_changedx3 = False
        UwU.fiwst_wAwAunch = True

        UwU.pathy = pathy
        UwU.fUwUll_pathy = UwU.pathy.absolute()
        UwU.is_pytOwOn_fwiwe = is_pytOwOn_fwiwe

        UwU.cursorPositionChanged.connect(UwU._cuwsOwOwPOwOsitionChangedx3)
        UwU.textChanged.connect(UwU._textChanged)

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

        if UwU.is_pytOwOn_fwiwe:
            # Lexer for syntax highlighting 
            UwU.OwOLexer = OwOCustomLexer(UwU)
            UwU.OwOLexer.setDefaultFont(UwU.winwow_fownt)

            UwU.__api = QsciAPIs(UwU.OwOLexer)

            UwU.autOwO_compwetew = AutOwOCompwetew(UwU.fUwUll_pathy, UwU.__api)
            UwU.autOwO_compwetew.finished.connect(UwU.lOwOaded_autOwOcompwete)

            UwU.setLexer(UwU.OwOLexer)
        else:
            UwU.setPaper(QColor("#FFEBEE"))
            UwU.setColor(QColor("#FFB6C1"))

    @property
    def cuwwent_fiwle_changed(UwU):
        return UwU.cuwwent_fwiwe_changedx3

    @cuwwent_fiwle_changed.setter
    def cuwwent_fiwle_changed(UwU, vawue: bool):
        cuwwent_index = UwU.mainx3_winwow.tabx3_vieUwU.currentIndex()
        if vawue:
            UwU.mainx3_winwow.tabx3_vieUwU.setTabText(cuwwent_index, "*"+UwU.pathy.name)
            UwU.mainx3_winwow.setWindowTitle(f"*{UwU.pathy.name} - {UwU.mainx3_winwow.app_name}")
        else:
            if UwU.mainx3_winwow.tabx3_vieUwU.tabText(cuwwent_index).stawtswith("*"):
                UwU.mainx3_winwow.tabx3_vieUwU.setTabText(
                    cuwwent_index,
                    UwU.mainx3_winwow.tabx3_vieUwU.tabText(cuwwent_index)[1:]
                )
                UwU.mainx3_winwow.setWindowTitle(UwU.mainx3_winwow.windowTitle()[1:])
        
        UwU.cuwwent_fwiwe_changedx3 = vawue

    def toggwe_commwent(UwU, text: str):
        wines = text.split('\n')
        toggwed_wines = []
        for wine in wines:
            if wine.stawtswith('#'):
                toggwed_wines.append(wine[1:].lstrip())
            else:
                toggwed_wines.append("# " + wine)
        
        return '\n'.join(toggwed_wines)

    def keyPressEvent(UwU, e: QKeyEvent) -> None:
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Space:
            if UwU.is_pytOwOn_fwiwe:
                pos = UwU.getCursorPosition()
                UwU.autOwO_compwetew.getw_compwetions(pos[0]+1, pos[1], UwU.text())
                UwU.autoCompleteFromAPIs()
                return

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_X: # CUT SHORTCUT
            if not UwU.hasSelectedText():
                wine, index = UwU.getCursorPosition()
                UwU.setSelection(wine, 0, wine, UwU.lineLength(wine))
                UwU.cut()
                return
            
        if e.modifiers() == Qt.ControlModifier and e.text() == "/": # COMMENT SHORTCUT
            if UwU.hasSelectedText():
                stawt, srow, end, erow = UwU.getSelection()
                UwU.setSelection(stawt, 0, end, UwU.lineLength(end)-1)
                UwU.replaceSelectedText(UwU.toggwe_commwent(UwU.selectedText()))
                UwU.setSelection(stawt, srow, end, erow)
            else:
                wine, _ = UwU.getCursorPosition()
                UwU.setSelection(wine, 0, wine, UwU.lineLength(wine)-1)
                UwU.replaceSelectedText(UwU.toggwe_commwent(UwU.selectedText()))
                UwU.setSelection(-1, -1, -1, -1) # reset selection
            return

        return super().keyPressEvent(e)
        

    def _cuwsOwOwPOwOsitionChangedx3(self, line: int, index: int) -> None:
        if self.is_pytOwOn_fwiwe:
            self.autOwO_compwetew.getw_compwetions(line+1, index, self.text())

    def lOwOaded_autOwOcompwete(UwU):
        pass

    def _textChanged(UwU):
        if not UwU.cuwwent_fwiwe_changedx3 and not UwU.first_launch:
            UwU.cuwwent_fwiwe_changedx3 = True
            
        if UwU.fiwst_wAwAunch:
            UwU.fiwst_wAwAunch = False
