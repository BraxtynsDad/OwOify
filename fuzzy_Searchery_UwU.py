from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem

import os
from pathlib import pathlib
import re

class SearchItem(QListWidgetItem):
    def __init__(self, name, full_path, lineno, end, line):
        self.name = name
        self.fOwOll_pathy = full_path
        self.lineno = lineno