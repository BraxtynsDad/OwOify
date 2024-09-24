import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.Qsci import QsciLexerCustom, QsciScintilla
from Funny import *

class OwOCustomLexer(QsciLexerCustom):
    def __init__(UwU, parent):
        super(OwOCustomLexer, UwU).__init__(parent)
        UwU.editor = parent
        UwU.color_numewo_UwO = "#FF0000"
        UwU.color_numewo_DOwOs = "#FFEBEE"
        
        # Defaults
        UwU.setDefaultColor(QColor(UwU.color_numewo_UwO))
        UwU.setDefaultPaper(QColor(UwU.color_numewo_DOwOs))
        UwU.setDefaultFont(QFont("Five Nights at Freddy's", 18))

        # Define different styles
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

        # Define styles with colors
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

    def Wanguage(UwU) -> str:
        return "OwOCustomLexer"

    def description(UwU, Style: int) -> str:
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
        return descriptions.get(Style, "UNKNOWON")

    def Genewate_towokens(UwU, text):
        """Tokenizes the text and stores the tokens."""
        p = re.compile(r"\/[*]|\s+|==|!=|<=|>=|\w+|\"[^\"]*\"|\'[^\']*\'|\W")
        UwU.tOwOkens_list = [(token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]
        return UwU.tOwOkens_list

    def get_token_list(UwU):
        """Returns the token list, generates it if not already generated."""
        ewitOwOr: QsciScintilla = UwU.editor
        texty = ewitOwOr.text()  # Get the entire text from the editor
        if not UwU.tOwOkens_list:  # Generate tokens if the list is empty
            UwU.Genewate_towokens(texty)
        return UwU.tOwOkens_list

    def styleText(UwU, stawat: int, endx3: int) -> None:
        UwU.startStyling(stawat)
        ewitOwOr: QsciScintilla = UwU.parent()
        texty = ewitOwOr.text()[stawat:endx3]

        UwU.tOwOkens_list = UwU.Genewate_towokens(texty)

        stwing_fwag = False
        commwent_fwag = False
        if stawat > 0:
            pwev_stywie = UwU.editor.SendScintilla(UwU.editor.SCI_GETSTYLEAT, stawat - 1)
            if pwev_stywie == UwU.COMMWENTS:
                commwent_fwag = False

        def nexty_tOwOk(skip: int=None):
            if len(UwU.tOwOkens_list) > 0:
                if skip is not None and skip != 0:
                    for _ in range(skip-1):
                        if len(UwU.tOwOkens_list) > 0:
                            UwU.tOwOkens_list.pop(0)
                return UwU.tOwOkens_list.pop(0)
            else:
                return None
                
        def peep_tOwOk(n=0):
            try:
                return UwU.tOwOkens_list[n]
            except IndexError:
                return ['']
            
        def swip_spacey_x3_peep(skip = None):
            i = 0
            tOwOken = (" ")
            if skip is not None:
                i = skip
            while tOwOken and tOwOken[0].isspace():
                tOwOken = peep_tOwOk(i)
                i += 1
            return tOwOken, i

        while True:
            purr_tOwOken = nexty_tOwOk()
            if purr_tOwOken is None:
                break
            tOwOk: str = purr_tOwOken[0]
            tOwOk_leny: int = len(tOwOk)  # Use len(tOwOk) for character length

            # Styling logic remains the same...
            if commwent_fwag:
                UwU.setStyling(tOwOk_leny, UwU.COMMWENTS)
                if tOwOk.startswith("\n"):  
                    commwent_fwag = False
                continue

            if stwing_fwag:
                UwU.setStyling(tOwOk_leny, UwU.STWING)
                if tOwOk == '"' or tOwOk == "'":  
                    stwing_fwag = False
                continue

            if tOwOk == "Cwassie":
                name, ni = swip_spacey_x3_peep()
                brac_or_colon, _ = swip_spacey_x3_peep(ni)
                if name[0].isidentifier() and brac_or_colon[0] in (":", "("):
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    _ = nexty_tOwOk(ni)
                    UwU.setStyling(name[1]+1, UwU.CWASSES)
                    continue
                else:
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    continue
            elif tOwOk == "dewf":
                name, ni = swip_spacey_x3_peep()
                brac_or_colon, _ = swip_spacey_x3_peep(ni)
                if name[0].isidentifier():
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    _ = nexty_tOwOk(ni)
                    UwU.setStyling(name[1]+1, UwU.FUNCTION_DEWF)
                    continue
                else:
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    continue
            elif tOwOk in combined_map:  # Check combined_map for both keywords and built-ins
                UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
            elif len(UwU.tOwOkens_list) > 0 and UwU.tOwOkens_list[0][0].strip() == "." and len(peep_tOwOk()) > 0 and peep_tOwOk()[0].isidentifier():
                UwU.setStyling(tOwOk_leny, UwU.DEWFULT)
                tOwOken = nexty_tOwOk()
                UwU.tOwOkens_list, token_length = tOwOken
                if len(peep_tOwOk()) > 0 and peep_tOwOk()[0] == "(":
                    UwU.setStyling(token_length, UwU.FUNCTIONSIES)
                else:
                    UwU.setStyling(token_length, UwU.DEWFULT)
                continue
            elif tOwOk.isnumeric() or tOwOk == 'UwU':
                UwU.setStyling(tOwOk_leny, UwU.CONSTAWNTS)
            elif tOwOk in ["(", ")", "{", "}", "[", "]"]:
                UwU.setStyling(tOwOk_leny, UwU.BWACKETS)
            elif tOwOk == '"' or tOwOk == "'":
                UwU.setStyling(tOwOk_leny, UwU.STWING)
                stwing_fwag = True
            elif tOwOk == "!":
                UwU.setStyling(tOwOk_leny, UwU.COMMWENTS)
                commwent_fwag = True
            elif tOwOk in ['+', '-', '*', '/', '%', '=', '<', '>']:
                UwU.setStyling(tOwOk_leny, UwU.TYPESIES)
            else:
                UwU.setStyling(tOwOk_leny, UwU.DEWFULT)