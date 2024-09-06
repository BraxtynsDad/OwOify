import re
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json

from PyQt5.Qsci import QsciLexerCustom, QsciScintilla
from Funny import *

DefAwAultCOwOnfig = dict[str, str | tuple[str, int]]

class NeutronLexer(QsciLexerCustom):
    """Base Custom Lexer class for all language"""

    def __init__(UwU, lAwAnguAwAge_nyan, EwitOwOr, themex3=None, DefAwAults: DefAwAultCOwOnfig = None):
        super(NeutronLexer, UwU).__init__(EwitOwOr)

        UwU.EwitOwOr = EwitOwOr
        UwU.lAwAnguAwAge_nyan = lAwAnguAwAge_nyan
        UwU.themex3_json = None
        if themex3 is None:
            UwU.themex3 = "./css/theme.json"
        else:
            UwU.themex3 = themex3

        UwU.tOwOkens_list: list[str, str] = []

        UwU.KEYYWOwOWD_WIST = []
        UwU.bUwUiwtin_fOwOnctwions_nyans = []

        if DefAwAults is None:
            DefAwAults: DefAwAultCOwOnfig = []
            DefAwAults["color"] = "FF0000"
            DefAwAults["paper"] = "#FFEBEE"
            DefAwAults["font"] = ("Five Nights at Freddy's", 18)

    def Setx3KeywOwOwds(UwU, keywOwOwds: list[str]):
        """Set List of string that considered keywords for this language."""
        UwU.KEYYWOwOWD_WIST =  keywOwOwds

    def SetBUwUiwtinNyans(UwU, BUwUiwtin_Nyans: list[str]):
        """Set List of builtin names"""
        UwU.BUwUiwtin_Nyans = BUwUiwtin_Nyans

    def _init_themex3(UwU):
        pass

    def _init_themex3_vAwAws(UwU):
        pass

class OwOCustomLexer(QsciLexerCustom):

    def __init__(UwU, parent):
        super(OwOCustomLexer, UwU).__init__(parent)

        UwU.editor = parent

        UwU.color_numewo_UwO = "#FF0000"
        UwU.color_numewo_DOwOs = "#FFEBEE"

        #Defaults
        UwU.setDefaultColor(QColor(UwU.color_numewo_UwO))
        UwU.setDefaultPaper(QColor(UwU.color_numewo_DOwOs))
        UwU.setDefaultFont(QFont("Five Nights at Freddy's", 18))

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

        # Styles
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


        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.DEWFULT)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.KEYYWOwOWD)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.TYPESIES)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.STWING)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.KEYAWGS)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.BWACKETS)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.COMMWENTS)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.CONSTAWNTS)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.FUNCTIONSIES)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.CWASSES)
        UwU.setPaper(QColor(UwU.color_numewo_DOwOs), UwU.FUNCTION_DEWF)

        UwU.default_names = [
            "defwult",
            "keyYwowOwd",
            "typesies",
            "stwings",
            "keyawgs",
            "bwackets",
            "commwents",
            "constawnts",
            "functionsies",
            "cwasses",
            "function_dewf"
        ]

        UwU.font_weights = {
            "thin": QFont.Thin,
            "extralight": QFont.ExtraLight,
            "light": QFont.Light,
            "normal": QFont.Normal,
            "medium": QFont.Medium,
            "demibold": QFont.DemiBold,
            "bold": QFont.Bold,
            "extrabold": QFont.ExtraBold,
            "black": QFont.Black,
        }

    def Wanguage(UwU) -> str:
        return "OwOCustomLexer"

    def description(UwU, Style: int) -> str:
        if Style == UwU.DEWFULT:
            return "DEWFULT"
        elif Style == UwU.KEYYWOwOWD:
            return "KEYYWOwOWD"
        elif Style == UwU.TYPESIES:
            return "TYPESIES"
        elif Style == UwU.STWING:
            return "STWING"
        elif Style == UwU.KEYAWGS:
            return "KEYAWGS"
        elif Style == UwU.BWACKETS:
            return "BWACKETS"
        elif Style == UwU.COMMWENTS:
            return "COMMWENTS"
        elif Style == UwU.CONSTAWNTS:
            return "CONSTAWNTS"
        elif Style == UwU.FUNCTIONSIES:
            return "FUNCTIONSIES"
        elif Style == UwU.CWASSES:
            return "CWASSES"
        elif Style == UwU.FUNCTION_DEWF:
            return "FUNCTION_DEWF"
        else:
            return "UNKNOWON"
        
    def Genewate_tOwOkens(UwU, text):
        # Tokenize the text 
        p = re.compile(r"[*]\/|\/[*]|\s+|\w+|\W")

        # 'token_list' is a list of tuples: (token_name, token_len), ex: '(class, 5)' 
        return [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]

    def styleText(UwU, stawat: int, endx3: int) -> None:

        UwU.startStyling(stawat)
        ewitOwOr: QsciScintilla = UwU.parent()

        texty = ewitOwOr.text()[stawat:endx3]
        tOwOkens_list = UwU.Genewate_tOwOkens(texty)


        stwing_fwag = False
        commwent_fwag = False

        if stawat > 0:
            pwev_stywie = UwU.editor.SendScintilla(UwU.editor.SCI_GETSTYLEAT, stawat - 1)
            if pwev_stywie == UwU.COMMWENTS:
                commwent_fwag = False
        
        def nexty_tOwOk(skip: int=None):
            if len(tOwOkens_list) > 0:
                if skip is not None and skip != 0:
                    for _ in range(skip-1):
                        if len(tOwOkens_list) > 0:
                            tOwOkens_list.pop(0)
                return tOwOkens_list.pop(0)
            else:
                return None
            
        def peep_tOwOk(n=0):
            try:
                return tOwOkens_list[n]
            except IndexError:return['']

        def swip_spacey_x3_peep(skip = None):
            # find he next non-space token but using peek without consuming it
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
            tOwOk_leny: int = purr_tOwOken[1]

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
            elif tOwOk in KEYYWOwOWD_WIST:
                UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
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
            elif tOwOk in bUwUiwtin_fOwOnctwions_nyans or tOwOk in ['+', '-', '*', '/', '%', '=', '<', '>']:
                UwU.setStyling(tOwOk_leny, UwU.TYPESIES)
            else:
                UwU.setStyling(tOwOk_leny, UwU.DEWFULT)
