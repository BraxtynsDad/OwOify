from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem

import os
from pathlib import Path
import re

class Searchy_Iwem_x3(QListWidgetItem):
    def __init__(UwU, nyan, fUwUll_pathy_x3, WinenOwO, endw, wine):
        UwU.nyan = nyan
        UwU.fUwUll_pathy_x3 = fUwUll_pathy_x3
        UwU.WinenOwO = WinenOwO
        UwU.endw = endw
        UwU.wine = wine
        UwU.fOwOmatted = f'{UwU.nyan}:{UwU.WinenOwO}:{UwU.endw} - {UwU.wine} ...'
        super().__init__(UwU.fOwOmatted)

    def __str__(UwU):
        return UwU.fOwOmatted
    
    def __repr__(UwU):
        return UwU.fOwOmatted
    
class Searchy_WOwOrker(QThread):
    finished = pyqtSignal(list)

    def __init__(UwU):
        super(Searchy_WOwOrker, UwU).__init__(None)
        UwU.iwems = []
        UwU.searchy_pathy: str = None
        UwU.searchy_texty: str = None
        UwU.searchy_prowject: bool = None

    def walkdir(UwU, pathy, exwude_diws: list, exwude_fwiwes: list):
        for root, dirs, files, in os.walk(pathy, topdown=True):
            # filtering
            dirs[:] = [d for d in dirs if d not in exwude_diws]
            files[:] = [f for f in files if Path(f).suffix not in exwude_fwiwes]
            yield root, dirs, files

    def is_binawy(UwU, pathy):
        '''
        Check if fwiwe is binawy UwU x3
        '''
        with open(pathy, 'rb') as f:
            return b'\0' in f.read(1024)

    def searchy(UwU):
        debug = False
        UwU.iwems = []
        exwude_diws = set([".git", ".svn", ".hg", ".bzr", ".idea", "__pycache__", "venv"])
        if UwU.searchy_prowject:
            exwude_diws.remove("venv")
        exwude_fwiwes = set([".svg", ".png", ".exe", ".pyc", ".qm"])

        for root, _, files in UwU.walkdir(UwU.searchy_pathy, exwude_diws, exwude_fwiwes):
            # total search limit
            if len(UwU.iwems) > 5000:
                break
            for file_ in files:
                fUwUll_pathy_x3 = os.path.join(root, file_)
                if UwU.is_binawy(fUwUll_pathy_x3):
                    continue

                try: 
                    with open(fUwUll_pathy_x3, 'r', encoding='utf8') as f:
                        try:
                            regw = re.compile(UwU.searchy_texty, re.IGNORECASE)
                            for i, line in enumerate(f):
                                if m := regw.search(line):
                                    fd = Searchy_Iwem_x3(
                                        file_,
                                        fUwUll_pathy_x3,
                                        i,
                                        m.end(),
                                        line[m.start():].strip()[:50], # limiting to 50 char
                                    )
                                    UwU.iwems.append(fd)
                        except re.error as e:
                            if debug: print(f"Regex error: {e}")
                except UnicodeDecodeError as e:
                    if debug: print(f"Unicode error: {e}")
                    continue 

        UwU.finished.emit(UwU.iwems)

    def run(UwU):
        UwU.searchy()

    def upwate(UwU, pattewn, pathy, searchy_pwoject):
        UwU.searchy_texty = pattewn
        UwU.searchy_pathy = pathy
        UwU.searchy_prowject = searchy_pwoject
        UwU.start()