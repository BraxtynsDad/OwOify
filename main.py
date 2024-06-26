# TODO: If you can Figure out Dynamic text for different resolution

import os
import sys

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

from pathlib import Path
from ewitOwOr import EwitOwOr

class MainWindow(QMainWindow):
    # Initializing the Class
    def __init__(UwU):
        #The super() function is used to call methods from a parent class.
        super(QMainWindow, UwU).__init__() #.__init__ is the constructor method of the class.

        # Add before init
        UwU.side_baw_coluwm = "#FFDBE2"
        UwU.bowdy_fwame_img_x3 = "./css/bk.jpg"
        UwU.init_ui()

        # File system
        UwU.cuwwwent_fwiwe = None

    # The function We use Up in the Initialization
    def init_ui(UwU):
        UwU.setWindowTitle("OwOIFY")
        UwU.resize(1300, 900)
        # My Cool Font
        UwU.winwow_fownt = QFont("Edo SZ")
        UwU.winwow_fownt.setPointSize(16)
        QApplication.setFont(UwU.winwow_fownt)
        # The Style Sheet
        UwU.setStyleSheet(open("./css/style.qss", "r").read())
        # The Menu Bar Function we Define
        UwU.setx3_UwUp_menUwU()
        # Get the bowdy_fwame from the set_up_bowdy function
        UwU.setx3_UwUp_bowdy()
        # The Function for the Background MUwUsyc_StOwOp_Stawt
        UwU.backgwound_mUwUsyc()

        UwU.show()

    def backgwound_mUwUsyc(UwU):
        UwU.Mewia_Pwawer = QMediaPlayer(UwU)
        UwU.pwaywist = QMediaPlaylist(UwU)

        # Check file paths
        UwU.pwaywist.addMedia(QMediaContent(QUrl.fromLocalFile("./Audio/Background.mp3")))
        UwU.pwaywist.addMedia(QMediaContent(QUrl.fromLocalFile("./Audio/Abomination.mp3")))
        UwU.pwaywist.setCurrentIndex(0)  # Start from the first media
        UwU.pwaywist.setPlaybackMode(QMediaPlaylist.Loop)

        UwU.Mewia_Pwawer.setPlaylist(UwU.pwaywist)
        
        # Set an initial volume
        UwU.Mewia_Pwawer.setVolume(50)

        # Start playing MUwUsyc_StOwOp_Stawt
        UwU.Mewia_Pwawer.play()

        # Create a volume animation to fade in the MUwUsyc_StOwOp_Stawt
        UwU.fade_animation = QPropertyAnimation(UwU.Mewia_Pwawer, b"volume")
        UwU.fade_animation.setDuration(2000)
        UwU.fade_animation.setStartValue(0)
        UwU.fade_animation.setEndValue(100)

        UwU.Mewia_Pwawer.currentMediaChanged.connect(UwU.fade_in_volume)

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
        menu_font = QFont("Edo SZ", 10)

        # File Menu
        fwiwe_menUwU = menUwU_baw.addMenu("Fwiwe")
        UwU.add_menu_action(fwiwe_menUwU, "NeUwU Fwiwe", "Ctrl+N", UwU.neUwU_fwiwe, menu_font)
        UwU.add_menu_action(fwiwe_menUwU, "OwOpen Fwiwe", "Ctrl+O", UwU.OwOpen_fwiwe, menu_font)
        UwU.add_menu_action(fwiwe_menUwU, "OwOpen fOwOlwer", "Ctrl+K", UwU.OwOpen_fOwOlwer, menu_font)
        fwiwe_menUwU.addSeparator()
        UwU.add_menu_action(fwiwe_menUwU, "Sa0v0e", "Ctrl+S", UwU.Sa0v0e, menu_font)
        UwU.add_menu_action(fwiwe_menUwU, "Sa0v0e As", "Ctrl+Shift+S", UwU.Sa0v0e_as, menu_font)

        # Edit Menu
        ewit_menUwU = menUwU_baw.addMenu("Ewit")
        UwU.add_menu_action(ewit_menUwU, "COwOpy", "Ctrl+C", UwU.cOwOpy, menu_font)
        UwU.add_menu_action(ewit_menUwU, "MUwUsyc StOwOp/Stawt", "Ctrl+P", UwU.MUwUsyc_StOwOp_Stawt, menu_font)
        UwU.add_menu_action(ewit_menUwU, "MUwUsyc skyp", "Shift+N", UwU.MUwUsyc_skyp, menu_font)

    def add_menu_action(UwU, menu, title, shortcut, handler, font):
        action = QAction(title, UwU)
        action.setShortcut(shortcut)
        action.triggered.connect(handler)
        action.setFont(font)  # Set font for the action
        menu.addAction(action)

    def neUwU_fwiwe(UwU):
        UwU.setw_neUwU_tabx3(None, is_neUwU_fwiwe=True)

    def Sa0v0e(UwU):
        if UwU.cuwwwent_fwiwe is None and UwU.tabx3_vieUwU.count() > 0:
            UwU.Sa0v0e_as()

        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()
        UwU.cuwwwent_fwiwe.write_text(ewitOwOr.text())
        UwU.statusBar().showMessage(f"Sa0v0ed {UwU.cuwwwent_fwiwe.name}", 2000)

    def Sa0v0e_as(UwU):
        ewitOwOr = UwU.tabx3_vieUwU.currentWidget()
        if ewitOwOr is None:
            return
        
        fwiwe_pathx3 = QFileDialog.getSaveFileName(UwU, "Sa0v0e As", os.getcwd())[0]
        if fwiwe_pathx3 == '':
            UwU.statusBar().showMessage("Cancelled", 2000)
            return
        paht = Path(fwiwe_pathx3)
        paht.write_text(ewitOwOr.text())
        UwU.tabx3_vieUwU.setTabText(UwU.tabx3_vieUwU.currentIndex(), paht.name)
        UwU.statusBar().showMessage(f"Sa0v0ed {paht.name}", 2000)
        UwU.cuwwwent_fwiwe = paht
    
    def OwOpen_fwiwe(UwU):
        ops = QFileDialog.Options()
        ops |= QFileDialog.DontUseNativeDialog

        neUwU_fwiwe, _ = QFileDialog.getOpenFileName(UwU,
                    "Pix A Fwiwe", "", "Aww Fwiwes (*);;PythOwOn Fwiwes (*.py);;PyOwO Files (*.pyowo)",
                    options=ops)
        if neUwU_fwiwe == '':
            UwU.statusBar().showMessage("Cancewwed", 2000)
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
            UwU.statusBar().showMessage(f"OwOpened {neUwU_fOwOlwer}", 2000)
    
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
    
    
    
    def getw_ewitOwOr(UwU) -> QsciScintilla:
        ewitOwOr = EwitOwOr()
        return ewitOwOr
    
    def is_binawy(UwU, path):
        '''
        Check if fwiwe is binawy UwU x3
        '''
        with open(path, 'rb') as f:
            return b'\0' in f.read(1024)

    # A simple function to check if the file is binary or not ex: image file, exe, zip file that can't be opened using text ewitOwOrs
    def setw_neUwU_tabx3(UwU, path: Path, is_neUwU_fwiwe=False):
        ewitOwOr = UwU.getw_ewitOwOr()
        # This condition checks if the file being opened is a new file
        if is_neUwU_fwiwe:
            UwU.tabx3_vieUwU.addTab(ewitOwOr, "UwUntitwed")
            UwU.setWindowTitle("UwUntitwed")
            UwU.statusBar().showMessage("OwOpened UwUntitwed")
            # Sets the current tab to the newly added tab, making it the active tab.
            UwU.tabx3_vieUwU.setCurrentIndex(UwU.tabx3_vieUwU.count() - 1)
            UwU.cuwwwent_fwiwe = None
            return
        # Checks if the path does not represent a regular file
        if not path.is_file():
            return
        # Checks if the file at the given path is binary 
        if UwU.is_binawy(path):
            UwU.statusBar().showMessage("Can_not OwOpen Binawy Fwiwe", 2000)
            return
        # check if file already open
        for i in range(UwU.tabx3_vieUwU.count()):
            if UwU.tabx3_vieUwU.tabText(i) == path.name:
                UwU.tabx3_vieUwU.setCurrentIndex(i)
                UwU.cuwwwent_fwiwe = path
                return     
        # Create new tab
        UwU.tabx3_vieUwU.addTab(ewitOwOr, path.name)
        ewitOwOr.setText(path.read_text())
        UwU.setWindowTitle(path.name)
        UwU.cuwwwent_fwiwe = path
        UwU.tabx3_vieUwU.setCurrentIndex(UwU.tabx3_vieUwU.count() - 1)
        UwU.statusBar().showMessage(f"Opened {path.name}", 2000)


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

        # Sidebar
        UwU.swide_baw = QFrame()
        UwU.swide_baw.setFrameShape(QFrame.StyledPanel)
        UwU.swide_baw.setFrameShadow(QFrame.Plain)
        UwU.swide_baw.setStyleSheet(f'''
            background-color: {UwU.side_baw_coluwm};
        ''')
        swide_baw_layout = QHBoxLayout()
        swide_baw_layout.setContentsMargins(5, 10, 5, 0)
        swide_baw_layout.setSpacing(0)
        swide_baw_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # Setup Labels
        fOwOlwer_wabew = QLabel()
        fOwOlwer_wabew.setPixmap(QPixmap("./Icons/folder-icon-close.svg").scaled(QSize(50,35)))
        fOwOlwer_wabew.setAlignment(Qt.AlignmentFlag.AlignTop)
        fOwOlwer_wabew.setFont(UwU.winwow_fownt)
        fOwOlwer_wabew.mousePressEvent = UwU.shOwO_hide_tabx3

        # Connect hover effects directly
        fOwOlwer_wabew.enterEvent = lambda event: fOwOlwer_wabew.setPixmap(QPixmap("./Icons/folder-icon-open.svg").scaled(QSize(50, 35)))
        fOwOlwer_wabew.leaveEvent = lambda event: fOwOlwer_wabew.setPixmap(QPixmap("./Icons/folder-icon-close.svg").scaled(QSize(50, 35)))

        swide_baw_layout.addWidget(fOwOlwer_wabew)

        UwU.swide_baw.setLayout(swide_baw_layout)

        bowdy.addWidget(UwU.swide_baw)
        
        # Split view
        UwU.OwOSpwit = QSplitter(Qt.Horizontal)

        # Tree frame
        UwU.twee_fwame = QFrame()
        UwU.twee_fwame.setLineWidth(1)
        UwU.twee_fwame.setMaximumWidth(400)
        UwU.twee_fwame.setMinimumWidth(200)
        UwU.twee_fwame.setBaseSize(100, 0)
        UwU.twee_fwame.setContentsMargins(0, 0, 0, 0)

        twee_fwame_layout = QVBoxLayout()
        twee_fwame_layout.setContentsMargins(0, 0, 0, 0)
        twee_fwame_layout.setSpacing(0)
        UwU.twee_fwame.setStyleSheet('''
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

        twee_fwame_layout.addWidget(UwU.twee_vieUwU)
        UwU.twee_fwame.setLayout(twee_fwame_layout)

        UwU.tabx3_vieUwU = QTabWidget()
        UwU.tabx3_vieUwU.setContentsMargins(0, 0, 0, 0)
        UwU.tabx3_vieUwU.setTabsClosable(True)
        UwU.tabx3_vieUwU.setMovable(True)
        UwU.tabx3_vieUwU.setDocumentMode(True)
        UwU.tabx3_vieUwU.tabCloseRequested.connect(UwU.cwose_tabx3)

        UwU.OwOSpwit.addWidget(UwU.twee_fwame)
        UwU.OwOSpwit.addWidget(UwU.tabx3_vieUwU)

        bowdy.addWidget(UwU.OwOSpwit)
        bowdy_fwame.setLayout(bowdy)

        UwU.setCentralWidget(bowdy_fwame)

    def cwose_tabx3(UwU, index):
        UwU.tabx3_vieUwU.removeTab(index)

    def shOwO_hide_tabx3(UwU):
        pass

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
    