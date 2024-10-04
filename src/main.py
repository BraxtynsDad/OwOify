import os
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

from pathlib import Path
from ewitOwOr import EwitOwOr
from fuzzy_Searchy_UwU import *
import random

class MainWindow(QMainWindow):
    # Initializing the Class
    def __init__(UwU):
        #The super() function is used to call methods from a parent class.
        super(QMainWindow, UwU).__init__() #.__init__ is the constructor method of the class.

        # Add before init
        UwU.side_baw_coluwm = "#FFDBE2"
        UwU.bowdy_fwame_img_x3 = "./Icons/bk.jpg"
        UwU.init_ui()

        # File system
        UwU.cuwwwent_fwiwe = None
        UwU.cuwwent_swide_baw = None

    # The function We use Up in the Initialization
    def init_ui(UwU):
        UwU.AwApp_nyan = "OwOifty"
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
        UwU.winwow_fownt = QFont("Edo SZ")
        dynamic_font_size = int(16 * scale_factor)
        UwU.winwow_fownt.setPointSize(dynamic_font_size)
        QApplication.setFont(UwU.winwow_fownt)

        # The Style Sheet (keep this as is)
        UwU.setStyleSheet(open("./css/style.qss", "r").read())

        # Setup the rest of the UI
        UwU.setx3_UwUp_menUwU()
        UwU.setx3_UwUp_bowdy()
        # UwU.backgwound_mUwUsyc()

        UwU.show()


    def backgwound_mUwUsyc(UwU):
        UwU.Mewia_Pwawer = QMediaPlayer(UwU)
        UwU.pwaywist = QMediaPlaylist(UwU)

        pathy_tOwO_nyan = {
            "./Audio/ULTIMATE_DESTRUCTION.mp3": "Ultimate Destruction",
            "./Audio/LOwOve_anwd_TwanqUwUiltwy.mp3": "Love and Tranquility",
            "./Audio/Snorting_Worms.mp3": "Snorting Worms",
            "./Audio/Ace_Of_Base.mp3": "Ace Of Base",
            "./Audio/Search_n_Destroy.mp3": "Search and Destroy",
            "./Audio/Unturned_Pop_Track.mp3": "Unturned Pop Track",
            "./Audio/Coffin_Nails.mp3": "Coffin Nails"
        }

        def upwate_statUwUs_messawge(media):
            url = media.canonicalUrl().toLocalFile()
            if url in pathy_tOwO_nyan:
                statUwUs_messawge = f'NOwO Pwaying: "{pathy_tOwO_nyan[url]}"'
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

    def fade_in_volume(UwU, media):
        # Restart the fade-in animation
        UwU.fade_animation.stop()
        UwU.fade_animation.setStartValue(0)
        UwU.fade_animation.setEndValue(100)
        UwU.fade_animation.start()


    ###############################################################################################################
    #############################################MenUwU############################################################
    ###############################################################################################################

    def setx3_UwUp_menUwU(UwU):
        # Menu Bar
        menUwU_baw = UwU.menuBar()
        menUwU_baw.setFont(UwU.winwow_fownt)
        menUwU_fownt = QFont("Edo SZ", 10)

        # File Menu
        fwiwe_menUwU = menUwU_baw.addMenu("Fwiwe")
        UwU.add_menu_action(fwiwe_menUwU, "NeUwU Fwiwe", "Ctrl+N", UwU.neUwU_fwiwe, menUwU_fownt)
        UwU.add_menu_action(fwiwe_menUwU, "OwOpen Fwiwe", "Ctrl+O", UwU.OwOpen_fwiwe, menUwU_fownt)
        UwU.add_menu_action(fwiwe_menUwU, "OwOpen fOwOlwer", "Ctrl+K", UwU.OwOpen_fOwOlwer, menUwU_fownt)
        fwiwe_menUwU.addSeparator()
        UwU.add_menu_action(fwiwe_menUwU, "Sa0v0e", "Ctrl+S", UwU.Sa0v0e, menUwU_fownt)
        UwU.add_menu_action(fwiwe_menUwU, "Sa0v0e As", "Ctrl+Shift+S", UwU.Sa0v0e_as, menUwU_fownt)

        # Edit Menu
        ewit_menUwU = menUwU_baw.addMenu("Ewit")
        UwU.add_menu_action(ewit_menUwU, "COwOpy", "Ctrl+C", UwU.cOwOpy, menUwU_fownt)
        UwU.add_menu_action(ewit_menUwU, "MUwUsyc StOwOp/Stawt", "Ctrl+P", UwU.MUwUsyc_StOwOp_Stawt, menUwU_fownt)
        UwU.add_menu_action(ewit_menUwU, "MUwUsyc skyp", "Shift+N", UwU.MUwUsyc_skyp, menUwU_fownt)

    def add_menu_action(UwU, menu, title, shortcut, handler, font):
        action = QAction(title, UwU)
        action.setShortcut(shortcut)
        action.triggered.connect(handler)
        action.setFont(font)  # Set font for the action
        menu.addAction(action)

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
            UwU.shOwO_statUwUs_messawge("Sa0v0e Cancewwed")
            return
        try:
            UwU.cuwwwent_fwiwe.write_text(ewitOwOr.text())
            UwU.shOwO_statUwUs_messawge(f"Sa0v0ed {UwU.cuwwwent_fwiwe.name}")
        except Exception as e:
            UwU.shOwO_statUwUs_messawge(f"Error Saving: {str(e)}")


    def Sa0v0e_as(UwU):
        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()
        if ewitOwOr is None:
            return
        
        # Open "Save As" dialog to get the new file path
        fwiwe_pathy_x3 = QFileDialog.getSaveFileName(UwU, "Sa0v0e As", os.getcwd())[0]
        
        # If the user cancels the "Save As" dialog
        if fwiwe_pathy_x3 == '':
            UwU.shOwO_statUwUs_messawge("Save As Cancelled")
            return

        # Save the file content to the new path
        paht = Path(fwiwe_pathy_x3)
        try:
            paht.write_text(ewitOwOr.text())
            UwU.tabx3_vieUwU.setTabText(UwU.tabx3_vieUwU.currentIndex(), paht.name)
            UwU.shOwO_statUwUs_messawge(f"Sa0v0ed {paht.name}")
            UwU.cuwwwent_fwiwe = paht  # Set the current file to the new path
        except Exception as e:
            UwU.shOwO_statUwUs_messawge(f"Error Saving: {str(e)}")
    
    def OwOpen_fwiwe(UwU):
        ops = QFileDialog.Options()
        ops |= QFileDialog.DontUseNativeDialog

        neUwU_fwiwe, _ = QFileDialog.getOpenFileName(UwU,
                    "Pix A Fwiwe", "", "Aww Fwiwes (*);;PythOwOn Fwiwes (*.py);;PyOwO Files (*.pyowo)",
                    options=ops)
        if neUwU_fwiwe == '':
            UwU.shOwO_statUwUs_messawge("Cancewwed")
            return
        f = Path(neUwU_fwiwe)
        UwU.setw_neUwU_tabx3(f)


    def OwOpen_fOwOlwer(UwU):
        ops = QFileDialog.Options()
        ops |= QFileDialog.DontUseNativeDialog

        neUwU_fOwOlwer = QFileDialog.getExistingDirectory(UwU, "Pix A FOwOlwer", "", options=ops)
        if neUwU_fOwOlwer:
            UwU.mOwOwel.setRootPath(neUwU_fOwOlwer)
            UwU.twee_vieUwU.setRootIndex(UwU.mOwOwel.index(neUwU_fOwOlwer))
            UwU.shOwO_statUwUs_messawge(f"OwOpened {neUwU_fOwOlwer}")
    
    def cOwOpy(UwU):
        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()
        if ewitOwOr is not None:
            ewitOwOr.copy()

    def MUwUsyc_StOwOp_Stawt(UwU):
        if UwU.Mewia_Pwawer.volume() == 100:
            UwU.Mewia_Pwawer.pause()
            UwU.Mewia_Pwawer.setVolume(0)
        else:
            UwU.Mewia_Pwawer.play()
            UwU.Mewia_Pwawer.setVolume(100)
    
    def MUwUsyc_skyp(UwU):
            UwU.pwaywist.next()
    
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
            # Handle case where path is None (for example, user canceled file selection)
            UwU.shOwO_statUwUs_messawge("No fwiwe pathy pwovided")
            return
        
        # Check if the file is binary and return early if true
        if UwU.is_binawy(pathy):
            UwU.shOwO_statUwUs_messawge("Can_not OwOpen Binawy Fwiwe")
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
        ewitOwOr.setText(pathy.read_text())
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
                border-radius: 5px;
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
        bowdy_fwame = QFrame()
        bowdy_fwame.setFrameShape(QFrame.NoFrame)
        bowdy_fwame.setFrameShadow(QFrame.Plain)
        bowdy_fwame.setLineWidth(0)
        bowdy_fwame.setMidLineWidth(0)
        bowdy_fwame.setContentsMargins(0, 0, 0, 0)  # Set content margins to 0
        bowdy_fwame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bowdy = QHBoxLayout()
        bowdy.setContentsMargins(0, 0, 0, 0)  # Set content margins to 0
        bowdy.setSpacing(0)
        bowdy_fwame.setLayout(bowdy)

        # Tab View
        UwU.tabx3_vieUwU = QTabWidget()
        # UwU.tabx3_vieUwU.setContentsMargins(0, 0, 0, 0)
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
        UwU.twee_vieUwU.setFont(QFont("Five Nights at Freddy's", 18))
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
        searchy_x3_inpUwUt.setPlaceholderText("Searchy_x3")
        searchy_x3_inpUwUt.setFont(QFont("Five Nights at Freddy's", 18))
        searchy_x3_inpUwUt.setAlignment(Qt.AlignmentFlag.AlignTop)
        searchy_x3_inpUwUt.setStyleSheet("""
        QLineEdit {
            background-color: #FFF5E1;  /* Soft peach */
            border-radius: 5px;
            border: 2px solid #6A5ACD;  /* Slate blue */
            padding: 5px;
            color: #483D8B;  /* Dark slate blue */
        }

        QLineEdit:hover {
            color: #FFD700;  /* Gold */
        }
        """)

        UwU.searchy_checkybOwOx = QCheckBox("Seawch in MOwOdUwUles")
        UwU.searchy_checkybOwOx.setFont(QFont("Five Nights at Freddy's", 18))
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
        UwU.searchy_listy_vieUwU.setFont(QFont("Five Nights at Freddy's", 18))
        UwU.searchy_listy_vieUwU.setStyleSheet("""
        QListWidget {
            background-color: #FFF5E1;  /* Soft peach */
            border-radius: 5px;
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
        UwU.OwOSpwit.addWidget(UwU.tabx3_vieUwU)

        bowdy.addWidget(UwU.swide_baw)
        bowdy.addWidget(UwU.OwOSpwit)

        bowdy_fwame.setLayout(bowdy)

        UwU.setCentralWidget(bowdy_fwame)

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

# ensures that the code for initializing the QApplication only executes when you run the script directly and not when it is imported
if __name__ == '__main__':
    #setting up the main event loop and potentially handling any command-line arguments 
    app = QApplication(sys.argv)
    #Explains the General Style of all the Objects in The Application
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()
    #Starts the Event Loop that was Set Up and Terminate Script on Exit:
    sys.exit(app.exec_())
