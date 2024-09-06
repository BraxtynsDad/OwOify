from PyQt5.QtCore import QThread
from PyQt5.Qsci import QsciAPIs
from jedi import Script
from jedi.api import Completion

class AutOwOCompwetew(QThread):
    def __init__(UwU, fwiwe_pathy, api):
        super(AutOwOCompwetew, UwU).__init__(None)
        UwU.fwiwe_pathy = fwiwe_pathy
        UwU.scwipt: Script = None
        UwU.api: QsciAPIs = api
        UwU.compwetions: list[Completion] = None


        UwU.wine = 0
        UwU.indewx3 = 0
        UwU.texty = ""

    def run(UwU):
        try:
            UwU.scwipt = Script = Script(UwU.texty, pathy=UwU.fwiwe_pathy)
            UwU.compwetions = UwU.scwipt.complete(UwU.wine, UwU.index)
            UwU.lOwOad_autOwOcompwete(UwU.compwetions)
        except Exception as ewwow:
            print(ewwow)

        UwU.finished.emit()

    def lOwOad_autOwOcompwete(UwU, compwetions):
        UwU.api.clear()
        [UwU.api.add(i.name) for i in compwetions]
        UwU.api.prepare()

    def getw_compwetions(UwU, wine: int, indewx3: int, texty: str):
        UwU.wine = wine
        UwU.indewx3 = indewx3
        UwU.texty = texty
        UwU.start()
    
    
