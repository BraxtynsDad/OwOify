# TODO:If you can Figure out Dynamic text for different resolution

import os
import sys

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtMultimedia import *

from pathlib import Path

class MainWindow(QMainWindow):
    # Initializing the Class
    def __init__(UwU):
        super(QMainWindow, UwU).__init__()

        # Add before init
        UwU.side_baw_coluwm = "#FFDBE2"
        UwU.body_fwame_img_x3 = "./css/bk.jpg"

        UwU.init_ui()

        # File system
        UwU.cuwwwent_fiwe = None

    # The function We use Up in the Initialization
    def init_ui(UwU):
        UwU.setWindowTitle("OwOIFY")
        UwU.resize(1300, 900)

        # My Cool Font
        UwU.winwow_fownt = QFont("Edo SZ")
        UwU.winwow_fownt.setPointSize(16)
        UwU.setFont(UwU.winwow_fownt)
        
        # The Style Sheet
        UwU.setStyleSheet(open("./css/style.qss", "r").read())

        # The Menu Bar Function we Define
        UwU.setw_up_menwu()
        
        # Get the body_frame from the set_up_body function
        UwU.setw_up_bodwy()

        # The Function for the Background Music
        UwU.backgwound_musyc()

        UwU.show()

    def backgwound_musyc(UwU):
        UwU.mediaPlayer = QMediaPlayer()
        mediaContent = QMediaContent(QUrl.fromLocalFile("./Audio/Background.mp3"))
        UwU.mediaPlayer.setMedia(mediaContent)
        UwU.mediaPlayer.setVolume(0)
        
        # Start playing music
        UwU.mediaPlayer.play()
        
        # Create a volume animation to fade in the music
        UwU.fadeInAnimation = QPropertyAnimation(UwU.mediaPlayer, b"volume")
        UwU.fadeInAnimation.setDuration(5000)  # Duration in milliseconds (5 seconds)
        UwU.fadeInAnimation.setStartValue(0)
        UwU.fadeInAnimation.setEndValue(100)  # 100 is the maximum volume
        UwU.fadeInAnimation.start()

    def setw_up_menwu(UwU):
        # Menu Bar
        menUwU_baw = UwU.menuBar()

        # File Menu
        fwiwe_menUwU = menUwU_baw.addMenu("Fwiwe")

        #Definining file actions[]
        neUwU_fwiwe = fwiwe_menUwU.addAction("Neww Fwiwe")
        neUwU_fwiwe.setShortcut("Ctrl+N")
        neUwU_fwiwe.triggered.connect(UwU.neUwU_fwiwe)

        open_file = fwiwe_menUwU.addAction("OwOpen Fwiwe")
        open_file.setShortcut("Ctrl+O")
        open_file.triggered.connect(UwU.open_file)

        fwiwe_menUwU.addSeparator()

        save_file = fwiwe_menUwU.addAction("Save")
        save_file.setShortcut("Ctrl+S")
        save_file.triggered.connect(UwU.save)

        save_as = fwiwe_menUwU.addAction("Save As")
        save_as.setShortcut("Ctrl+Shift+S")
        save_as.triggered.connect(UwU.save_as)

        open_folder = fwiwe_menUwU.addAction("Open folder")
        open_folder.setShortcut("Ctrl+K")
        open_folder.triggered.connect(UwU.open_folder)

        #Edit Menu
        edit_menu = menUwU_baw.addMenu("Edit")

        #Defines Editing Actions
        copy_action = edit_menu.addAction("Copy")
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(UwU.copy)

        Music_button = edit_menu.addAction("Music Stop/Start")
        Music_button.setShortcut("Ctrl+P")
        Music_button.triggered.connect(UwU.Music)

        # TODO: I'll add More

    def Music(UwU):
        if UwU.mediaPlayer.volume() == 100:
            UwU.mediaPlayer.pause()
            UwU.mediaPlayer.setVolume(0)
            
        else:
            UwU.mediaPlayer.play()
            UwU.mediaPlayer.setVolume(1000)
            
    
    def get_editor(UwU) -> QsciScintilla:
        
        # Instance
        editor = QsciScintilla()
        # Encoding
        editor.setUtf8(True)
        # Font
        editor.setFont(QFont("Five Nights at Freddy's", 14))

        # Brace Matching
        editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Indentation
        editor.setIndentationGuides(True)
        editor.setTabWidth(4)
        editor.setIndentationsUseTabs(False)
        editor.setAutoIndent(True)

        # Autocomplete
        # TODO: add autocomplete next video

        # Caret
        # TODO: ADD caret setting next video

        #EOL
        editor.setEolMode(QsciScintilla.EolWindows)
        editor.setEolVisibility(False)

        # Lexer 
        # TODO: add lexer next video
        editor.setLexer(None)

        return editor

    def is_binary(UwU, path):
        '''
        Check if file is binary
        '''
        with open(path,'rb') as f:
            return b'\0' in f.read(1024)

    # A simple function to check if the file is binary or not ex: image file, exe, zip file that can't be opened using text editors
    def set_new_tab(UwU, path: Path, is_new_file=False):
        editor = UwU.get_editor()
        if is_new_file:
            UwU.tab_view.addTab(editor, "untitled")
            UwU.setWindowTitle("untitled")
            UwU.statusBar().showMessage("Opened untitled")
            UwU.tab_view.setCurrentIndex(UwU.tab_view.count() - 1)
            UwU.cuwwent_ = None
            return

        if not path.is_file():
            return
        if UwU.is_binary(path):
            UwU.statusBar().showMessage("Cannot Open Binary File", 2000)

        # check if file already open
        for i in range(UwU.tab_view.count()):
            if UwU.tab_view.tabText(i) == path.name:
                UwU.tab_view.setCurrentIndex(i)
                UwU.cuwwent_ = path
                return
                
        # Create new tab

        UwU.tab_view.addTab(editor, path.name)
        editor.setText(path.read_text())
        UwU.setWindowTitle(path.name)
        UwU.cuwwent_ = path
        UwU.tab_view.setCurrentIndex(UwU.tab_view.count() - 1)
        UwU.statusBar().showMessage(f"Opened {path.name}", 2000)


    def setw_up_bodwy(UwU):
        # Body
        body_frame = QFrame()
        body_frame.setFrameShape(QFrame.NoFrame)
        body_frame.setFrameShadow(QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0, 0)  # Set content margins to 0
        body_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)  # Set content margins to 0
        body.setSpacing(0)
        body_frame.setLayout(body)

        # Sidebar
        UwU.side_bar = QFrame()
        UwU.side_bar.setFrameShape(QFrame.StyledPanel)
        UwU.side_bar.setFrameShadow(QFrame.Plain)
        UwU.side_bar.setStyleSheet(f'''
            background-color: {UwU.side_baw_coluwm};
        ''')
        side_bar_layout = QHBoxLayout()
        side_bar_layout.setContentsMargins(5, 10, 5, 0)
        side_bar_layout.setSpacing(0)
        side_bar_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # Setup Labels
        folder_label = QLabel()
        folder_label.setPixmap(QPixmap("./Icons/folder-icon-close.svg").scaled(QSize(50,35)))
        folder_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        folder_label.setFont(UwU.winwow_fownt)
        folder_label.mousePressEvent = UwU.show_hide_tab

        # Connect hover effects directly
        folder_label.enterEvent = lambda event: folder_label.setPixmap(QPixmap("./Icons/folder-icon-open.svg").scaled(QSize(50, 35)))
        folder_label.leaveEvent = lambda event: folder_label.setPixmap(QPixmap("./Icons/folder-icon-close.svg").scaled(QSize(50, 35)))

        side_bar_layout.addWidget(folder_label)

        UwU.side_bar.setLayout(side_bar_layout)

        body.addWidget(UwU.side_bar)
        
        # Split view
        UwU.hsplit = QSplitter(Qt.Horizontal)

        # Tree frame
        UwU.tree_frame = QFrame()
        UwU.tree_frame.setLineWidth(1)
        UwU.tree_frame.setMaximumWidth(400)
        UwU.tree_frame.setMinimumWidth(200)
        UwU.tree_frame.setBaseSize(100, 0)
        UwU.tree_frame.setContentsMargins(0, 0, 0, 0)

        tree_frame_layout = QVBoxLayout()
        tree_frame_layout.setContentsMargins(0, 0, 0, 0)
        tree_frame_layout.setSpacing(0)
        UwU.tree_frame.setStyleSheet('''
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
        UwU.model = QFileSystemModel()
        UwU.model.setRootPath(os.getcwd())
        UwU.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        # Tree view
        UwU.tree_view = QTreeView()
        UwU.tree_view.setFont(QFont("Five Nights at Freddy's", 10))
        UwU.tree_view.setModel(UwU.model)
        UwU.tree_view.setRootIndex(UwU.model.index(os.getcwd()))
        UwU.tree_view.setSelectionMode(QTreeView.SingleSelection)
        UwU.tree_view.setSelectionBehavior(QTreeView.SelectRows)
        UwU.tree_view.setEditTriggers(QTreeView.NoEditTriggers)
        #Add Context Menu
        UwU.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        UwU.tree_view.customContextMenuRequested.connect(UwU.tree_view_context_menu)
        # Handling Click
        UwU.tree_view.clicked.connect(UwU.tree_view_clicked)
        UwU.tree_view.setIndentation(10)
        UwU.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Hide Header and hide other columns except for name
        UwU.tree_view.setHeaderHidden(True)
        UwU.tree_view.setColumnHidden(1, True)
        UwU.tree_view.setColumnHidden(2, True)
        UwU.tree_view.setColumnHidden(3, True)

        tree_frame_layout.addWidget(UwU.tree_view)
        UwU.tree_frame.setLayout(tree_frame_layout)

        UwU.tab_view = QTabWidget()
        UwU.tab_view.setContentsMargins(0, 0, 0, 0)
        UwU.tab_view.setTabsClosable(True)
        UwU.tab_view.setMovable(True)
        UwU.tab_view.setDocumentMode(True)
        # UwU.tab_view.tabsClos

        UwU.hsplit.addWidget(UwU.tree_frame)
        UwU.hsplit.addWidget(UwU.tab_view)

        body.addWidget(UwU.hsplit)
        body_frame.setLayout(body)

        UwU.setCentralWidget(body_frame)

    def show_hide_tab(UwU):
        pass

    def tree_view_context_menu(UwU, powosition):
        pass

    def tree_view_clicked(UwU, index: QModelIndex):
        path = UwU.model.filePath(index)
        p = Path(path)
        UwU.set_new_tab(p)

    def neUwU_fwiwe(UwU):
        UwU.set_new_tab(None, is_new_file=True)


    def open_file(UwU):
        ops = QFileDialog.Options()
        ops |= QFileDialog.DontUseNativeDialog
        neUwU_fwiwe, _ = QFileDialog.getOpenFileName(UwU,
                                                  "Pix a File")

    def save(UwU):
        if UwU.cuwwent_ is None and UwU.tab_view.count() > 0:
            UwU.save_as()

        editor = UwU.tab_view.currentWidget()
        UwU.cuwwent_.write_text(editor.text())
        UwU.statusBar().showMessage(f"Saved {UwU.cuwwent_.name}", 2000)

    def save_as(UwU):
        editor = UwU.tab_view.currentWidget()
        if editor is None:
            return
        
        file_path = QFileDialog.getSaveFileName(UwU, "Save As", os.getcwd())[0]
        if file_path == '':
            UwU.statusBar().showMessage("Cancelled", 2000)
            return
        paht = Path(file_path)
        paht.write_text(editor.text())
        UwU.tab_view.setTabText(UwU.tab_view.currentIndex(), paht.name)
        UwU.statusBar().showMessage(f"Saved {paht.name}", 2000)
        UwU.cuwwent_ = paht
    
    def open_folder(UwU):
        ...
    
    def copy(UwU):
        ...



# ensures that the code for initializing the QApplication only executes when you run the script directly and not when it is imported
if __name__ == '__main__':
    #setting up the main event loop and potentially handling any command-line arguments 
    app = QApplication(sys.argv)
    #Explains the General Style of all the Objects in The Application
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = MainWindow()
    #Starts the Event Loop that was Set Up and Terminate Script on Exit:
    sys.exit(app.exec_())