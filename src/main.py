import os
import sys
import io
import contextlib

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget

from pathlib import Path
from ewitOwOr import EwitOwOr
from lexer import *
from Parser import OwOParser
from Interpreter import *
from terminal_widget import TerminalWidget
from fuzzy_Searchy_UwU import *
import random

class MainWindow(QMainWindow):
    # Initializing the Class
    def __init__(UwU):
        super(QMainWindow, UwU).__init__()  # .__init__ is the constructor method of the class.

        # Add before init
        UwU.side_baw_coluwm = "#FFDBE2"
        UwU.bowdy_fwame_img_x3 = "./Icons/bk.jpg"
        fnaf = QFontDatabase.addApplicationFont("./css/fnaf.ttf")
        edosz = QFontDatabase.addApplicationFont("./css/edosz.ttf")
        ms_pain = QFontDatabase.addApplicationFont("./css/MS_PAIN.ttf")
        UwU.edosz_families = QFontDatabase.applicationFontFamilies(edosz)
        UwU.fnaf_families = QFontDatabase.applicationFontFamilies(fnaf)
        UwU.ms_pain_families = QFontDatabase.applicationFontFamilies(ms_pain)
        UwU.old_pos = None  # For dragging the window
        UwU.init_ui()

        # File system
        UwU.cuwwwent_fwiwe = None
        UwU.cuwwent_swide_baw = None

    # The function We use Up in the Initialization
    def init_ui(UwU):
        UwU.AwApp_nyan = "OwOIFTY"
        # Remove the default window title bar
        UwU.setWindowFlags(Qt.FramelessWindowHint)
        # Set the window title (optional, won't be visible)
        UwU.setWindowTitle(UwU.AwApp_nyan)

        # Retrieve screen resolution
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Scale factor based on screen resolution (adjust as needed)
        scale_factor = min(screen_width / 1920, screen_height / 1080)

        # Resize window dynamically
        UwU.resize(int(1300 * scale_factor), int(900 * scale_factor))

        # Dynamically scale the font size
        UwU.winwow_fownt = QFont(UwU.edosz_families[0])
        dynamic_font_size = int(16 * scale_factor)
        UwU.winwow_fownt.setPointSize(dynamic_font_size)
        QApplication.setFont(UwU.winwow_fownt)

        # The Style Sheet (keep this as is)
        UwU.setStyleSheet(open("./css/style.qss", "r").read())

        # Add the terminal output area
        UwU.terminal_output = TerminalWidget()
        UwU.terminal_output.setFont(QFont("Comic Sans MS", 12))
        UwU.terminal_output.setStyleSheet("""
        QTextEdit {
            background-color: #1e1e1e;
            color: #d4d4d4;
        }
        """)
        UwU.terminal_output.input_submitted.connect(UwU.provide_input_to_interpreter)

        # Setup the rest of the UI
        UwU.create_custom_title_bar()
        UwU.setx3_UwUp_bowdy()
        UwU.backgwound_mUwUsyc()

        # Create a main layout to include the title bar and body
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(UwU.title_bar)
        main_layout.addWidget(UwU.bowdy_fwame)

        # Create a central widget to set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        UwU.setCentralWidget(central_widget)

        UwU.show()

    def create_custom_title_bar(UwU):
        # Create a widget to act as the custom title bar
        UwU.title_bar = QFrame()
        UwU.title_bar.setFixedHeight(40)  # Adjust as needed
        UwU.title_bar.setStyleSheet("""
        QFrame {
            background-color: #ff1fb0;  /* pink tanish color */
        }
        """)

        # Create a horizontal layout for the title bar
        title_bar_layout = QHBoxLayout()
        title_bar_layout.setContentsMargins(5, 0, 5, 0)
        title_bar_layout.setSpacing(5)

        # Create the two buttons with dropdown menus
        # First button (e.g., 'File')
        file_button = QPushButton("File")
        file_button.setFont(QFont(UwU.edosz_families[0], 14))
        file_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton::menu-indicator {
                image: none;
            }
            QPushButton:hover {
                color: #C724B1;
            }  
        """)
        file_menu = QMenu()
        UwU.add_menu_actions(file_menu, 'File')
        file_button.setMenu(file_menu)

        # Second button (e.g., 'Edit')
        edit_button = QPushButton("Help")
        edit_button.setFont(UwU.winwow_fownt)
        edit_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton::menu-indicator {
                image: none;
            }
            QPushButton:hover {
                color: #C724B1;
            }  
        """)
        edit_menu = QMenu()
        UwU.add_menu_actions(edit_menu, 'Music')
        edit_button.setMenu(edit_menu)

        # wun button
        UwU.wun_button = QPushButton("run")
        UwU.wun_button.setFont(QFont(UwU.ms_pain_families[0], 18))
        UwU.wun_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton:hover {
                color: #C724B1;
            }  
        """)
        UwU.wun_button.clicked.connect(UwU.wun_code)

        # Create the title label
        title_label = QLabel(UwU.AwApp_nyan)
        title_label.setFont(QFont("Comic Sans MS", 28))
        title_label.setStyleSheet("color: #FFFFFF;")  # Set text color to white
        title_label.setAlignment(Qt.AlignCenter)

        # Add utility buttons (e.g., minimize, maximize/restore, close)
        # Minimize button
        minimize_button = QPushButton("–")
        minimize_button.setFixedSize(30, 30)
        minimize_button.clicked.connect(UwU.showMinimized)
        minimize_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton:hover {
                color: #00FFFF;
            }                           
        """)

        # Maximize/Restore button
        UwU.is_maximized = False

        def toggle_max_restore():
            if UwU.isMaximized():
                UwU.showNormal()
                UwU.is_maximized = False
            else:
                UwU.showMaximized()
                UwU.is_maximized = True

        maximize_button = QPushButton("❐")
        maximize_button.setFixedSize(30, 30)
        maximize_button.clicked.connect(toggle_max_restore)
        maximize_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton:hover {
                color: #002d33;
            }
        """)

        # Close button
        close_button = QPushButton("✕")
        close_button.setFixedSize(30, 30)
        close_button.clicked.connect(UwU.close)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton:hover {
                color: #FF0000;
            }
        """)

        # Add widgets to the layout
        # Left side
        title_bar_layout.addWidget(file_button)
        title_bar_layout.addWidget(edit_button)
        title_bar_layout.addWidget(UwU.wun_button)

        # Add stretch to push title label to the center
        title_bar_layout.addStretch()

        # Title label
        title_bar_layout.addWidget(title_label)

        # Add stretch after title label
        title_bar_layout.addStretch()

        # Right side
        title_bar_layout.addWidget(minimize_button)
        title_bar_layout.addWidget(maximize_button)
        title_bar_layout.addWidget(close_button)

        UwU.title_bar.setLayout(title_bar_layout)

        # Implement mouse events for dragging
        UwU.title_bar.mousePressEvent = UwU.title_bar_mousePressEvent
        UwU.title_bar.mouseMoveEvent = UwU.title_bar_mouseMoveEvent
        UwU.title_bar.mouseReleaseEvent = UwU.title_bar_mouseReleaseEvent

    def add_menu_actions(UwU, menu, menu_type):
        menUwU_fownt = QFont(UwU.edosz_families[0], 10)
        if menu_type == 'File':
            UwU.add_menu_action(menu, "New File", "Ctrl+N", UwU.neUwU_fwiwe, menUwU_fownt)
            UwU.add_menu_action(menu, "Open File", "Ctrl+O", UwU.OwOpen_fwiwe, menUwU_fownt)
            UwU.add_menu_action(menu, "Open Folder", "Ctrl+K", UwU.OwOpen_fOwOlwer, menUwU_fownt)
            menu.addSeparator()
            UwU.add_menu_action(menu, "Save", "Ctrl+S", UwU.Sa0v0e, menUwU_fownt)
            UwU.add_menu_action(menu, "Save As", "Ctrl+Shift+S", UwU.Sa0v0e_as, menUwU_fownt)
        elif menu_type == 'Music':
            UwU.add_menu_action(menu, "Musyc Stop/Start", "Ctrl+P", UwU.MUwUsyc_StOwOp_Stawt, menUwU_fownt)
            UwU.add_menu_action(menu, "Musyc skyp", "Shift+N", UwU.MUwUsyc_skyp, menUwU_fownt)
            UwU.add_menu_action(menu, "Clear Console", "Ctrl+T", UwU.clr_cOwOnsOwOle, menUwU_fownt)
            UwU.add_menu_action(menu, "Help", "Ctrl+H", UwU.Hewp_txt, menUwU_fownt)
            UwU.add_menu_action(menu, "Video Help", "Shift+Y", UwU.Start_VideOwO, menUwU_fownt)

    def add_menu_action(UwU, menu, title, shortcut, handler, font):
        action = QAction(title, UwU)
        action.setShortcut(shortcut)
        action.triggered.connect(handler)
        action.setFont(font)  # Set font for the action
        menu.addAction(action)
    
    def clr_cOwOnsOwOle(UwU):
        UwU.terminal_output.clear()
        UwU.terminal_output.append("(´• ω •`)>")

    def title_bar_mousePressEvent(UwU, event):
        if event.button() == Qt.LeftButton:
            UwU.old_pos = event.globalPos() - UwU.frameGeometry().topLeft()
            event.accept()

    def title_bar_mouseMoveEvent(UwU, event):
        if event.buttons() == Qt.LeftButton and UwU.old_pos is not None:
            UwU.move(event.globalPos() - UwU.old_pos)
            event.accept()

    def title_bar_mouseReleaseEvent(UwU, event):
        UwU.old_pos = None
        event.accept()

    ###############################################################################################################
    #############################################Menu Actions######################################################
    ###############################################################################################################

    def neUwU_fwiwe(UwU):
        UwU.setw_neUwU_tabx3(None, is_neUwU_fwiwe=True)

    def shOwO_statUwUs_messawge(UwU, message):
        UwU.statusBar().show()
        UwU.statusBar().showMessage(message)
        QTimer.singleShot(5000, UwU.hide_status_bar)

    def hide_status_bar(UwU):
        UwU.statusBar().clearMessage()
        UwU.statusBar().hide()

    def Sa0v0e(UwU):
        if UwU.cuwwwent_fwiwe is None and UwU.tabx3_vieUwU.count() > 0:
            UwU.Sa0v0e_as()
            return
        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()

        if UwU.cuwwwent_fwiwe is None:
            UwU.shOwO_statUwUs_messawge("Save Cancewwed")
            return
        try:
            UwU.cuwwwent_fwiwe.write_text(ewitOwOr.text())
            UwU.shOwO_statUwUs_messawge(f"Saved {UwU.cuwwwent_fwiwe.name}")
        except Exception as e:
            UwU.shOwO_statUwUs_messawge(f"Error Saving: {str(e)}")

    def Sa0v0e_as(UwU):
        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()
        if ewitOwOr is None:
            return

        dialog = QFileDialog(UwU, "Sa0v0e As", os.getcwd())
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFont(QFont("Comic Sans MS", 12))
        if dialog.exec_() == QFileDialog.Accepted:
            fwiwe_pathy_x3 = dialog.selectedFiles()[0]
        else:
            UwU.shOwO_statUwUs_messawge("Save As Cancelled")
            return

        if fwiwe_pathy_x3 == '':
            UwU.shOwO_statUwUs_messawge("Save As Cancelled")
            return

        paht = Path(fwiwe_pathy_x3)
        try:
            paht.write_text(ewitOwOr.text())
            UwU.tabx3_vieUwU.setTabText(UwU.tabx3_vieUwU.currentIndex(), paht.name)
            UwU.shOwO_statUwUs_messawge(f"Sa0v0ed {paht.name}")
            UwU.cuwwwent_fwiwe = paht
        except Exception as e:
            UwU.shOwO_statUwUs_messawge(f"Error Saving: {str(e)}")

    def OwOpen_fwiwe(UwU):
        ops = QFileDialog.Options()
        ops |= QFileDialog.DontUseNativeDialog

        dialog = QFileDialog(UwU, "Pix A Fwiwe", "")
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setOption(QFileDialog.ReadOnly, True)
        dialog.setNameFilter("Aww Fwiwes (*);;PythOwOn Fwiwes (*.py);;PyOwO Files (*.pyowo)")
        dialog.setFont(QFont("Comic Sans MS", 12))  # Set font to Comic Sans
        if dialog.exec_() == QFileDialog.Accepted:
            neUwU_fwiwe = dialog.selectedFiles()[0]
        else:
            UwU.shOwO_statUwUs_messawge("Cancewwed")
            return

        if neUwU_fwiwe == '':
            UwU.shOwO_statUwUs_messawge("Cancewwed")
            return
        f = Path(neUwU_fwiwe)
        UwU.setw_neUwU_tabx3(f)


    def OwOpen_fOwOlwer(UwU):
        ops = QFileDialog.Options()
        ops |= QFileDialog.DontUseNativeDialog

        dialog = QFileDialog(UwU, "Pix A FOwOlwer", "")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setFont(QFont("Comic Sans MS", 12))
        if dialog.exec_() == QFileDialog.Accepted:
            neUwU_fOwOlwer = dialog.selectedFiles()[0]
        else:
            UwU.shOwO_statUwUs_messawge("Cancewwed")
            return

        if neUwU_fOwOlwer:
            UwU.mOwOwel.setRootPath(neUwU_fOwOlwer)
            UwU.twee_vieUwU.setRootIndex(UwU.mOwOwel.index(neUwU_fOwOlwer))
            UwU.shOwO_statUwUs_messawge(f"OwOpened {neUwU_fOwOlwer}")

    def MUwUsyc_StOwOp_Stawt(UwU):
        if UwU.Mewia_Pwawer.volume() == 100:
            UwU.Mewia_Pwawer.pause()
            UwU.Mewia_Pwawer.setVolume(0)
        else:
            UwU.Mewia_Pwawer.play()
            UwU.Mewia_Pwawer.setVolume(100)

    def MUwUsyc_skyp(UwU):
            UwU.pwaywist.next()

    def Hewp_txt(UwU):
        UwU.setw_neUwU_tabx3(Path("./src/Help.txt"), is_neUwU_fwiwe=False)


    def backgwound_mUwUsyc(UwU):
        UwU.Mewia_Pwawer = QMediaPlayer(UwU)
        UwU.pwaywist = QMediaPlaylist(UwU)

        pathy_tOwO_nyan = {
            "./Media/ULTIMATE_DESTRUCTION.mp3": "Ultimate Destruction",
            "./Media/LOwOve_anwd_TwanqUwUiltwy.mp3": "Love and Tranquility",
            "./Media/Snorting_Worms.mp3": "Snorting Worms",
            "./Media/Ace_Of_Base.mp3": "Ace Of Base",
            "./Media/Search_n_Destroy.mp3": "Search and Destroy",
            "./Media/Unturned_Pop_Track.mp3": "Unturned Pop Track",
            "./Media/Coffin_Nails.mp3": "Coffin Nails"
        }

        def upwate_statUwUs_messawge(media):
            url = media.canonicalUrl().toLocalFile()
            if url in pathy_tOwO_nyan:
                statUwUs_messawge = f'Now Playing: "{pathy_tOwO_nyan[url]}"'
                UwU.statusBar().showMessage(statUwUs_messawge)
                    
        UwU.pwaywist.currentMediaChanged.connect(upwate_statUwUs_messawge)

        media_list = list(pathy_tOwO_nyan.keys())
        random.shuffle(media_list)

        print("Shuffled Order:")
        for path in media_list:
            print(pathy_tOwO_nyan[path])

        for path in media_list:
            UwU.pwaywist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))

        UwU.pwaywist.setPlaybackMode(QMediaPlaylist.Loop)
        UwU.pwaywist.setCurrentIndex(0)

        UwU.Mewia_Pwawer.setPlaylist(UwU.pwaywist)
        UwU.Mewia_Pwawer.setVolume(50)

        # Create a volume animation to fade in the music
        UwU.fade_animation = QPropertyAnimation(UwU.Mewia_Pwawer, b"volume")
        UwU.fade_animation.setDuration(2000)
        UwU.fade_animation.setStartValue(0)
        UwU.fade_animation.setEndValue(100)

        UwU.Mewia_Pwawer.play()
        UwU.fade_animation.start()
    
    def getw_ewitOwOr(UwU, file_extension=None) -> QsciScintilla:
        ewitOwOr = EwitOwOr(UwU, file_extension)
        return ewitOwOr

    
    def is_binawy(UwU, pathy):
        # Check if path is a file and not a directory
        if not os.path.isfile(pathy):
            # If it's not a file, return False
            return False

        try:
            with open(pathy, 'rb') as f:
                fwead = f.read(1024)
                # Check for non-text bytes (binary data)
                if b'\0' in fwead:
                    return True
                else:
                    return False
        except Exception as e:
            # Handle any exceptions, like permission issues
            print(f"Error weading file: {e}")
            return False

    # A simple function to check if the file is binary or not ex: image file, exe, zip file that can't be opened using text ewitOwOrs
    def setw_neUwU_tabx3(UwU, pathy: Path, is_neUwU_fwiwe=False):
        # If this is a new file, handle it separately
        if is_neUwU_fwiwe:
            # Assume new untitled files are .pyowo files
            ewitOwOr = UwU.getw_ewitOwOr('.pyowo')
            UwU.tabx3_vieUwU.addTab(ewitOwOr, "UwUntitwed")
            UwU.setWindowTitle("UwUntitwed - " + UwU.AwApp_nyan)
            UwU.shOwO_statUwUs_messawge("OwOpened UwUntitwed")
            UwU.tabx3_vieUwU.setCurrentIndex(UwU.tabx3_vieUwU.count() - 1)
            UwU.cuwwwent_fwiwe = None  # No file associated with new untitled file
            return

        # Handle existing files
        if pathy is None:
            UwU.shOwO_statUwUs_messawge("No fwiwe pathy pwovided")
            return

        # Check if the file is binary and return early if true
        if UwU.is_binawy(pathy):
            UwU.shOwO_statUwUs_messawge("Cannot open binary file.")
            return

        if not pathy.is_file():
            return

        # Get the file extension
        file_extension = pathy.suffix.lower()

        # Check if the file is already open
        for i in range(UwU.tabx3_vieUwU.count()):
            if UwU.tabx3_vieUwU.tabText(i) == pathy.name:
                UwU.tabx3_vieUwU.setCurrentIndex(i)
                UwU.cuwwwent_fwiwe = pathy
                return

        # Create new tab for existing file
        ewitOwOr = UwU.getw_ewitOwOr(file_extension)
        UwU.tabx3_vieUwU.addTab(ewitOwOr, pathy.name)
        try:
            # Try reading the file with common encodings
            file_content = UwU.read_file_with_encodings(pathy)
        except UnicodeDecodeError as e:
            UwU.shOwO_statUwUs_messawge(f"Error reading file: {str(e)}")
            return

        ewitOwOr.setText(file_content)
        UwU.setWindowTitle(f"{pathy.name} - {UwU.AwApp_nyan}")
        UwU.cuwwwent_fwiwe = pathy
        UwU.tabx3_vieUwU.setCurrentIndex(UwU.tabx3_vieUwU.count() - 1)
        UwU.shOwO_statUwUs_messawge(f"Opened {pathy.name}")

        # This condition checks if the file being opened is a new file
        if is_neUwU_fwiwe:
            UwU.tabx3_vieUwU.addTab(ewitOwOr, "UwUntitwed")
            UwU.setWindowTitle("UwUntitwed - " + UwU.AwApp_nyan)
            UwU.shOwO_statUwUs_messawge("OwOpened UwUntitwed")
            UwU.tabx3_vieUwU.setCurrentIndex(UwU.tabx3_vieUwU.count() - 1)
            UwU.cuwwwent_fwiwe = None
            return

        # Check if the file is already open
        for i in range(UwU.tabx3_vieUwU.count()):
            if UwU.tabx3_vieUwU.tabText(i) == pathy.name:
                UwU.tabx3_vieUwU.setCurrentIndex(i)
                UwU.cuwwwent_fwiwe = pathy
                return
        
        # Create new tab
        UwU.tabx3_vieUwU.addTab(ewitOwOr, pathy.name)
        ewitOwOr.setText(pathy.read_text())
        UwU.setWindowTitle(f"{pathy.name} - {UwU.AwApp_nyan}")
        UwU.cuwwwent_fwiwe = pathy
        UwU.tabx3_vieUwU.setCurrentIndex(UwU.tabx3_vieUwU.count() - 1)
        UwU.shOwO_statUwUs_messawge(f"Opened {pathy.name}")


    def read_file_with_encodings(UwU, pathy, encodings=['utf-8', 'latin-1', 'cp1252']):
        for encoding in encodings:
            try:
                return pathy.read_text(encoding=encoding)
            except UnicodeDecodeError:
                continue
        raise UnicodeDecodeError(f"Unable to read file {pathy.name} with common encodings.")

    def setw_cowsOwO_pointy_x3(UwU, e):
        UwU.setCursor(Qt.PointingHandCursor)

    def setw_cowsOwO_awwowOwO(UwU, e):
        UwU.setCursor(Qt.ArrowCursor)

    def getw_swide_baw_wabew(UwU, pathy, name):
        wabew = QLabel()
        wabew.setPixmap(QPixmap(pathy).scaled(QSize(70,70)))
        wabew.setAlignment(Qt.AlignmentFlag.AlignTop)
        wabew.setFont(UwU.winwow_fownt)
        wabew.mousePressEvent = lambda e: UwU.shOwO_hide_tabx3(e, name)
        wabew.enterEvent = UwU.setw_cowsOwO_pointy_x3
        wabew.leaveEvent = UwU.setw_cowsOwO_awwowOwO
        return wabew
    
    def getw_fwame(UwU) -> QFrame:
        fwame = QFrame()
        fwame.setFrameShape(QFrame.NoFrame)
        fwame.setFrameShadow(QFrame.Plain)
        fwame.setContentsMargins(0, 0, 0, 0)
        fwame.setStyleSheet('''
            QFrame {
                background-color: #B662C5;
                border: none;
                padding: 5px;
                color: White;
            }
            QFrame:hover {
                color: #50B356;
            }
        ''')
        return fwame
    
    def shOwO_hide_tabx3(UwU, e, type_):
        print(type_)
        if type_ == "searchy_x3_icOwOn":
            if UwU.searchy_x3_fwame not in UwU.OwOSpwit.children():
                UwU.OwOSpwit.replaceWidget(0, UwU.searchy_x3_fwame)
        elif type_ == "fwiwe_manongew":
            if UwU.fwiwe_manongew_fwame not in UwU.OwOSpwit.children():
                UwU.OwOSpwit.replaceWidget(0, UwU.fwiwe_manongew_fwame)

        fwame = UwU.OwOSpwit.widget(0)
        if UwU.cuwwent_swide_baw == type_:
            if fwame.isVisible():
                fwame.hide()
            else:
                fwame.show()
        else:
            if not fwame.isVisible():
                fwame.show()
        UwU.cuwwent_swide_baw = type_

    def setx3_UwUp_bowdy(UwU):
        # Body
        UwU.bowdy_fwame = QFrame()
        bowdy_fwame = UwU.bowdy_fwame
        bowdy_fwame.setFrameShape(QFrame.NoFrame)
        bowdy_fwame.setFrameShadow(QFrame.Plain)
        bowdy_fwame.setLineWidth(0)
        bowdy_fwame.setMidLineWidth(0)
        bowdy_fwame.setContentsMargins(0, 0, 0, 0)  # Set content margins to 0
        bowdy_fwame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bowdy_fwame.setStyleSheet("background-color: transparent;")
        bowdy = QHBoxLayout()
        bowdy.setContentsMargins(0, 0, 0, 0)  # Set content margins to 0
        bowdy.setSpacing(0)
        bowdy_fwame.setLayout(bowdy)

        # Tab View
        UwU.tabx3_vieUwU = QTabWidget()
        UwU.tabx3_vieUwU.setTabsClosable(True)
        UwU.tabx3_vieUwU.setMovable(True)
        UwU.tabx3_vieUwU.setDocumentMode(True)
        UwU.tabx3_vieUwU.tabCloseRequested.connect(UwU.cwose_tabx3)

        # Sidebar
        UwU.swide_baw = QFrame()
        UwU.swide_baw.setFrameShape(QFrame.StyledPanel)
        UwU.swide_baw.setFrameShadow(QFrame.Plain)
        UwU.swide_baw.setStyleSheet(f'''
            background-color: {UwU.side_baw_coluwm};
        ''')
        swide_baw_wayout = QVBoxLayout()
        swide_baw_wayout.setContentsMargins(5, 10, 5, 0)
        swide_baw_wayout.setSpacing(0)
        swide_baw_wayout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # Setup Labels
        fOwOlwer_wabew = UwU.getw_swide_baw_wabew("./Icons/folder-icon-close.svg", "fwiwe_manongew")
        Seawch_Wabew = UwU.getw_swide_baw_wabew("./Icons/search-icon.svg", "searchy_x3_icOwOn")

        # Connect hover effects directly
        fOwOlwer_wabew.enterEvent = lambda event: fOwOlwer_wabew.setPixmap(QPixmap("./Icons/folder-icon-open.svg").scaled(QSize(70, 70)))
        fOwOlwer_wabew.leaveEvent = lambda event: fOwOlwer_wabew.setPixmap(QPixmap("./Icons/folder-icon-close.svg").scaled(QSize(70, 70)))

        swide_baw_wayout.addWidget(fOwOlwer_wabew)
        swide_baw_wayout.addWidget(Seawch_Wabew)
        UwU.swide_baw.setLayout(swide_baw_wayout)
        
        # Split view
        UwU.OwOSpwit = QSplitter(Qt.Horizontal)

        # Create a vertical splitter to hold the editor and terminal
        UwU.vertical_splitter = QSplitter(Qt.Vertical)
        UwU.vertical_splitter.addWidget(UwU.tabx3_vieUwU)
        UwU.vertical_splitter.addWidget(UwU.terminal_output)
        UwU.vertical_splitter.setSizes([600, 200])  # Adjust initial sizes

        # Tree frame
        UwU.fwiwe_manongew_fwame = UwU.getw_fwame()
        UwU.fwiwe_manongew_fwame.setMaximumWidth(400)
        UwU.fwiwe_manongew_fwame.setMinimumWidth(200)
        twee_fwame_layout = QVBoxLayout()
        twee_fwame_layout.setContentsMargins(0, 0, 0, 0)
        twee_fwame_layout.setSpacing(0)

        # Create file system model
        UwU.mOwOwel = QFileSystemModel()
        UwU.mOwOwel.setRootPath(os.getcwd())
        UwU.mOwOwel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        # Tree view
        UwU.twee_vieUwU = QTreeView()
        UwU.twee_vieUwU.setFont(QFont(UwU.fnaf_families[0], 18))
        UwU.twee_vieUwU.setModel(UwU.mOwOwel)
        UwU.twee_vieUwU.setRootIndex(UwU.mOwOwel.index(os.getcwd()))
        UwU.twee_vieUwU.setSelectionMode(QTreeView.SingleSelection)
        UwU.twee_vieUwU.setSelectionBehavior(QTreeView.SelectRows)
        UwU.twee_vieUwU.setEditTriggers(QTreeView.NoEditTriggers)
        #Add Context Menu
        UwU.twee_vieUwU.setContextMenuPolicy(Qt.CustomContextMenu)
        UwU.twee_vieUwU.customContextMenuRequested.connect(UwU.twee_vieUwU_cOwOntewxt_menUwU)
        # Handling Click
        UwU.twee_vieUwU.clicked.connect(UwU.twee_vieUwU_cwicked)
        UwU.twee_vieUwU.setIndentation(10)
        UwU.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Hide Header and hide other columns except for name
        UwU.twee_vieUwU.setHeaderHidden(True)
        UwU.twee_vieUwU.setColumnHidden(1, True)
        UwU.twee_vieUwU.setColumnHidden(2, True)
        UwU.twee_vieUwU.setColumnHidden(3, True)

        # Search View
        UwU.searchy_x3_fwame = UwU.getw_fwame()
        UwU.searchy_x3_fwame.setMaximumWidth(400)
        UwU.searchy_x3_fwame.setMinimumWidth(200)

        searchy_x3_layout = QVBoxLayout()
        searchy_x3_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        searchy_x3_layout.setContentsMargins(0, 10, 0, 0)
        searchy_x3_layout.setSpacing(0)

        searchy_x3_inpUwUt = QLineEdit()
        searchy_x3_inpUwUt.setPlaceholderText("Search")
        searchy_x3_inpUwUt.setFont(QFont(UwU.fnaf_families[0], 18))
        searchy_x3_inpUwUt.setAlignment(Qt.AlignmentFlag.AlignTop)
        searchy_x3_inpUwUt.setStyleSheet("""
        QLineEdit {
            background-color: #FFF5E1;  /* Soft peach */
            border: 2px solid #6A5ACD;  /* Slate blue */
            padding: 5px;
            color: #483D8B;  /* Dark slate blue */
        }

        QLineEdit:hover {
            color: #FFD700;  /* Gold */
        }
        """)

        UwU.searchy_checkybOwOx = QCheckBox("Search in Modules")
        UwU.searchy_checkybOwOx.setFont(QFont(UwU.fnaf_families[0], 18))
        UwU.searchy_checkybOwOx.setStyleSheet("color: #483D8B; margin-bottom: 10px")

        UwU.searchy_wOwOrker = Searchy_WOwOrker()
        UwU.searchy_wOwOrker.finished.connect(UwU.searchy_finishewd)
        searchy_x3_inpUwUt.textChanged.connect(
            lambda text: UwU.searchy_wOwOrker.upwate(
                text,
                UwU.mOwOwel.rootDirectory().absolutePath(),
                UwU.searchy_checkybOwOx.isChecked(),
            )
        )

        UwU.searchy_listy_vieUwU = QListWidget()
        UwU.searchy_listy_vieUwU.setFont(QFont(UwU.fnaf_families[0], 18))
        UwU.searchy_listy_vieUwU.setStyleSheet("""
        QListWidget {
            background-color: #FFF5E1;  /* Soft peach */
            border: 2px solid #6A5ACD;  /* Slate blue */
            padding: 5px;
            color: #483D8B;  /* Dark slate blue */                                      
        }
        """)

        UwU.searchy_listy_vieUwU.itemClicked.connect(UwU.searchy_listy_vieUwU_Cwicked)

        searchy_x3_layout.addWidget(UwU.searchy_checkybOwOx)
        searchy_x3_layout.addWidget(searchy_x3_inpUwUt)
        searchy_x3_layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Minimum))        

        twee_fwame_layout.addWidget(UwU.twee_vieUwU)
        UwU.fwiwe_manongew_fwame.setLayout(twee_fwame_layout)

        searchy_x3_layout.addWidget(UwU.searchy_listy_vieUwU)
        UwU.searchy_x3_fwame.setLayout(searchy_x3_layout)

        UwU.OwOSpwit.addWidget(UwU.fwiwe_manongew_fwame)
        UwU.OwOSpwit.addWidget(UwU.vertical_splitter)

        bowdy.addWidget(UwU.swide_baw)
        bowdy.addWidget(UwU.OwOSpwit)

        UwU.bowdy_fwame.setLayout(bowdy)

        UwU.setCentralWidget(UwU.bowdy_fwame)

    def wun_code(UwU):
        # Get the current editor
        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()
        if ewitOwOr is None:
            return

        # Disable the wun button to prevent multiple wuns
        UwU.wun_button.setEnabled(False)

        # Get the code from the editor
        code = ewitOwOr.text()

        # Move cursor to the end
        UwU.terminal_output.moveCursor(QTextCursor.End)

        # Parse the code
        tokens = OwOCustomLexer.Genewate_towokens(ewitOwOr, code)
        parser = OwOParser(tokens)
        ast = parser.parse()

        # Check for parsing errors
        if parser.errors:
            for error in parser.errors:
                UwU.terminal_output.append(f"\nParsing Error: {error['message']}")
            UwU.wun_button.setEnabled(True)
            return

        # Create and start the interpreter thread
        UwU.interpreter_thread = InterpreterThread(ast)
        UwU.interpreter_thread.request_input.connect(UwU.handle_input_request)
        UwU.interpreter_thread.output_signal.connect(UwU.handle_interpreter_output)
        UwU.interpreter_thread.finished.connect(UwU.interpreter_finished)
        UwU.interpreter_thread.ready_for_input.connect(UwU.set_standard_prompt)
        UwU.interpreter_thread.start()

    def handle_input_request(UwU, prompt):
        # Set the terminal's prompt to the input prompt
        UwU.terminal_output.set_prompt(prompt)
        # Set a flag indicating that input is expected
        UwU.terminal_output.expecting_input = True

    def provide_input_to_interpreter(UwU, input_text):
        if UwU.interpreter_thread:
            UwU.interpreter_thread.provide_input(input_text)
        else:
            pass  # Handle cases where no interpreter is wunning
    
    def set_standard_prompt(UwU):
        UwU.terminal_output.set_prompt(UwU.terminal_output.standard_prompt)

    def handle_interpreter_output(UwU, output_text):
        UwU.terminal_output.append_output(output_text)
        
    def interpreter_finished(UwU):
        # Set the prompt when interpreter finishes
        UwU.terminal_output.set_prompt(UwU.terminal_output.standard_prompt)
        UwU.terminal_output.moveCursor(QTextCursor.End)
        UwU.terminal_output.ensureCursorVisible()
        # Re-enable the wun button
        UwU.wun_button.setEnabled(True)

    def searchy_finishewd(UwU, iwems):
        UwU.searchy_listy_vieUwU.clear()
        for iwem in iwems:
            UwU.searchy_listy_vieUwU.addItem(iwem)

    def searchy_listy_vieUwU_Cwicked(UwU, iwem: Searchy_Iwem_x3):
        UwU.setw_neUwU_tabx3(Path(iwem.fUwUll_pathy_x3))
        ewitOwOr: EwitOwOr = UwU.tabx3_vieUwU.currentWidget()
        ewitOwOr.setCursorPosition(iwem.WinenOwO, iwem.endw)
        ewitOwOr.setFocus()
        

    def cwose_tabx3(UwU, index):
        UwU.tabx3_vieUwU.removeTab(index)

    def twee_vieUwU_cOwOntewxt_menUwU(UwU, powosition):
        pass

    def twee_vieUwU_cwicked(UwU, index: QModelIndex):
        path = UwU.mOwOwel.filePath(index)
        p = Path(path)
        UwU.setw_neUwU_tabx3(p)

    def Start_VideOwO(UwU):
        # Create a container widget that will hold both the video and controls
        video_container = QWidget()
        video_layout = QVBoxLayout()  # Layout for the video and controls

        # Create media player and video widget
        UwU.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        UwU.videoWidget = QVideoWidget()

        # Create video control buttons
        play_button = QPushButton("⏯")
        play_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton::menu-indicator {
                image: none;
            }
            QPushButton:hover {
                color: #C724B1;
            }  
        """)
        pause_button = QPushButton("⏸")
        pause_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton::menu-indicator {
                image: none;
            }
            QPushButton:hover {
                color: #C724B1;
            }  
        """)
        stop_button = QPushButton("⏹")
        stop_button.setStyleSheet("""
            QPushButton {
                background-color: none;
                color: #FFFFFF;
                border: none;
            }
            QPushButton::menu-indicator {
                image: none;
            }
            QPushButton:hover {
                color: #C724B1;
            }  
        """)

        # Create a slider for seeking through the video
        video_slider = QSlider(Qt.Horizontal)
        video_slider.setRange(0, 0)  # Initial range, will be updated later

        control_layout = QHBoxLayout()
        control_layout.addWidget(play_button)
        control_layout.addWidget(pause_button)
        control_layout.addWidget(stop_button)
        control_layout.addWidget(video_slider)

        video_layout.addWidget(UwU.videoWidget)
        video_layout.addLayout(control_layout)
        video_container.setLayout(video_layout)

        # Add the container widget to the tab view
        UwU.tabx3_vieUwU.addTab(video_container, "Video")

        # Set the video output to the video widget
        UwU.mediaPlayer.setVideoOutput(UwU.videoWidget)
        video_url = QUrl.fromLocalFile(str('./Media/Help.avi'))
        UwU.mediaPlayer.setMedia(QMediaContent(video_url))

        # Set slider to sync with video duration
        def on_duration_changed(duration):
            video_slider.setRange(0, duration)

        def on_position_changed(position):
            video_slider.setValue(position)

        # Connect mediaPlayer signals for slider functionality
        UwU.mediaPlayer.durationChanged.connect(on_duration_changed)
        UwU.mediaPlayer.positionChanged.connect(on_position_changed)

        # Connect slider to change video position when moved
        video_slider.sliderMoved.connect(UwU.mediaPlayer.setPosition)

        # Define the play, pause, and stop button functions
        play_button.clicked.connect(UwU.mediaPlayer.play)
        pause_button.clicked.connect(UwU.mediaPlayer.pause)
        stop_button.clicked.connect(UwU.mediaPlayer.stop)

        # Auto-play if not already playing
        if UwU.mediaPlayer.state() != QMediaPlayer.PlayingState:
            UwU.mediaPlayer.play()

# ensures that the code for initializing the QApplication only executes when you wun the script directly and not when it is imported
if __name__ == '__main__':
    # setting up the main event loop and potentially handling any command-line arguments
    app = QApplication(sys.argv)
    # Explains the General Style of all the Objects in The Application
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()
    # Starts the Event Loop that was Set Up and Terminate Script on Exit:
    sys.exit(app.exec_())
