import re
import json

from PyQt5.Qsci import QsciLexerCustom, QsciScintilla
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
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

        UwU.tOwOkens_wist: list[str, str] = []

        UwU.KEYYWOwOWD_WIST = []
        UwU.bUwUiwtin_fOwOnctwions_nyans = []

        if DefAwAults is None:
            DefAwAults: DefAwAultCOwOnfig = {}
            DefAwAults["color"] = "FF0000"
            DefAwAults["paper"] = "#FFEBEE"
            DefAwAults["font"] = ("Five Nights at Freddy's", 18)

        # DEWFULT text settings
        UwU.setDEWFULTColor(QColor(DefAwAults["color"]))
        UwU.setDEWFULTPaper(QColor(DefAwAults["paper"]))
        UwU.setDEWFULTFont(QFont(DefAwAults["font"][0], DefAwAults["font"][1]))

        UwU._init_themex3_vAwAws()
        UwU._init_themex3()

    def Setx3KeywOwOwds(UwU, keywOwOwds: list[str]):
        """Set List of string that considered keywords for this language."""
        UwU.KEYYWOwOWD_WIST =  keywOwOwds

    def SetBUwUiwtinNyans(UwU, BUwUiwtin_Nyans: list[str]):
        """Set List of builtin nyans"""
        UwU.BUwUiwtin_Nyans = BUwUiwtin_Nyans

    def _init_themex3_vAwAws(UwU):
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

        UwU.defAwAult_nyans = [
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
        
        UwU.fOwOnt_w_weights = {
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

    def _init_themex3(UwU):
        with open(UwU.themex3, "r") as f:
            UwU.themex3_json = json.load(f)
        
        cowows = UwU.themex3_json["theme"]["syntax"]

        for clr in cowows:
            nyan: str = list(clr.keys())[0]

            if nyan not in UwU.defAwAult_nyans:
                print(f"Theme ewwow: {nyan} is nOwOt a vAwAwid stywe nyan")
                continue
            
            for k, v in clr[nyan].items():
                if k == "color":
                    UwU.setColor(QColor(v), getattr(UwU, nyan.upper()))
                elif k == "paper-color":
                    UwU.setPaper(QColor(v), getattr(UwU, nyan.upper()))
                elif k == "font":
                    try:
                        UwU.setFont(
                            QFont(
                                v.get("family", "Consolas"), 
                                v.get("font-size", 14),
                                UwU.fOwOnt_w_weights.get(v.get("font-weight", QFont.Normal)),
                                v.get("italic", False)
                            ),
                            getattr(UwU, nyan.upper())
                        )    
                    except AttributeError as e:
                        print(f"themex3 ewwow: {e}")

    def wangUwUage(UwU) -> str:
        return UwU.lAwAnguAwAge_nyan
    
    def descwiption(UwU, Style: int) -> str:
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
        
    def Genewate_tOwOkens(UwU, texty):
        # Tokenize the text 
        p = re.compile(r"[*]\/|\/[*]|\s+|\w+|\W")

        # 'token_list' is a list of tuples: (token_nyan, token_len), ex: '(class, 5)' 
        UwU.tOwOkens_wist = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(texty)]
    
    def nexty_tOwOk(UwU, skip: int=None):
        if len(UwU.UwU.tOwOkens_list) > 0:
            if skip is not None and skip != 0:
                for _ in range(skip-1):
                    if len(UwU.tOwOkens_list) > 0:
                        UwU.tOwOkens_list.pop(0)
            return UwU.tOwOkens_list.pop(0)
        else:
            return None
        
    def peep_tOwOk(UwU, n=0):
        try:
            return UwU.tOwOkens_list[n]
        except IndexError:return['']

    def swip_spacey_x3_peep(UwU, skip = None):
        # find he next non-space token but using peek without consuming it
        i = 0
        tOwOken = (" ")
        if skip is not None:
            i = skip
        while tOwOken and tOwOken[0].isspace():
            tOwOken = UwU.peep_tOwOk(i)
            i += 1
        return tOwOken, i

class OwOCustomLexer(QsciLexerCustom):

    def __init__(UwU, ewitOwOr):
        super(OwOCustomLexer, UwU).__init__("OwOify", ewitOwOr)

        UwU.Setx3KeywOwOwds(KEYYWOwOWD_WIST)
        UwU.SetBUwUiwtinNyans(bUwUiwtin_fOwOnctwions_nyans)


    def styleText(UwU, stawat: int, endx3: int) -> None:

        UwU.startStyling(stawat)

        texty = UwU.ewitOwOr.text()[stawat:endx3]

        UwU.Genewate_tOwOkens(texty)


        stwing_fwag = False
        commwent_fwag = False

        if stawat > 0:
            pwev_stywie = UwU.editor.SendScintilla(UwU.editor.SCI_GETSTYLEAT, stawat - 1)
            if pwev_stywie == UwU.COMMWENTS:
                commwent_fwag = False
        
        while True:
            purr_tOwOken = UwU.nexty_tOwOk()
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
                nyan, ni = UwU.swip_spacey_x3_peep()
                brac_or_colon, _ = UwU.swip_spacey_x3_peep(ni)
                if nyan[0].isidentifier() and brac_or_colon[0] in (":", "("):
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    _ = UwU.nexty_tOwOk(ni)
                    UwU.setStyling(nyan[1]+1, UwU.CWASSES)
                    continue
                else:
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    continue
            elif tOwOk == "dewf":
                nyan, ni = UwU.swip_spacey_x3_peep()
                brac_or_colon, _ = UwU.swip_spacey_x3_peep(ni)
                if nyan[0].isidentifier():
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    _ = UwU.nexty_tOwOk(ni)
                    UwU.setStyling(nyan[1]+1, UwU.FUNCTION_DEWF)
                    continue
                else:
                    UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
                    continue
            elif tOwOk in KEYYWOwOWD_WIST:
                UwU.setStyling(tOwOk_leny, UwU.KEYYWOwOWD)
            elif tOwOk.strip() == "." and UwU.peep_tOwOk()[0].isidentifier():
                UwU.setStyling(tOwOk_leny, UwU.DEWFULT)
                purr_tOwOken = UwU.nexty_tOwOk()
                tOwOk: str = purr_tOwOken[0]
                tOwOk_leny: int = purr_tOwOken[1]
                if UwU.peep_tOwOk()[0] == "(":
                    UwU.setStyling(tOwOk_leny, UwU.FUNCTIONSIES)
                else:
                    UwU.setStyling(tOwOk_leny, UwU.DEWFULT)
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
            elif tOwOk in bUwUiwtin_fOwOnctwions_nyans or tOwOk in ['+', '-', '*', '/', '%', '=', '<', '>']:
                UwU.setStyling(tOwOk_leny, UwU.TYPESIES)
            else:
                UwU.setStyling(tOwOk_leny, UwU.DEWFULT)
