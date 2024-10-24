# terminal_widget.py
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QTextCursor

class TerminalWidget(QTextEdit):
    input_submitted = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.standard_prompt = "(´• ω •`)>"
        self.prompt = self.standard_prompt
        self.expecting_input = False
        self.prompt_pos = 0  # Position in the document where the prompt ends
        self.init_terminal()
        self.cursorPositionChanged.connect(self.ensure_cursor_in_allowed_area)

    def init_terminal(self):
        self.setReadOnly(False)
        self.set_prompt(self.prompt)

    def set_prompt(self, prompt_text):
        self.prompt = prompt_text
        self.moveCursor(QTextCursor.End)
        if not self.toPlainText().endswith('\n'):
            self.insertPlainText('\n')
        self.insertPlainText(self.prompt)
        self.moveCursor(QTextCursor.End)
        # Update prompt position to after the prompt
        self.prompt_pos = self.textCursor().position()
        self.ensureCursorVisible()

    def append_output(self, text):
        # Remove existing prompt if present
        cursor = self.textCursor()
        cursor.setPosition(self.prompt_pos)
        cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        if cursor.hasSelection():
            cursor.removeSelectedText()
        # Move cursor to end
        self.moveCursor(QTextCursor.End)
        # Insert newline if needed
        if not self.toPlainText().endswith('\n'):
            self.insertPlainText('\n')
        # Insert the output
        self.insertPlainText(text)
        # Update prompt position
        self.prompt_pos = self.textCursor().position()


    def keyPressEvent(self, event):
        cursor = self.textCursor()
        pos = cursor.position()
        # Prevent cursor from moving before prompt_pos
        if pos < self.prompt_pos:
            cursor.setPosition(self.prompt_pos)
            self.setTextCursor(cursor)

        if event.key() == Qt.Key_Backspace:
            if pos > self.prompt_pos:
                super().keyPressEvent(event)
            else:
                # Prevent backspace before prompt
                pass
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.expecting_input:
                user_input = self.get_current_input()
                self.input_submitted.emit(user_input)
                self.expecting_input = False
                # Do not reset the prompt here
            else:
                self.insertPlainText('\n')
                # Do not set the prompt here
            self.moveCursor(QTextCursor.End)
            self.ensureCursorVisible()
        else:
            super().keyPressEvent(event)
            # After processing, ensure cursor is not before prompt_pos
            cursor = self.textCursor()
            if cursor.position() < self.prompt_pos:
                cursor.setPosition(self.prompt_pos)
                self.setTextCursor(cursor)

    def mousePressEvent(self, event):
        cursor = self.cursorForPosition(event.pos())
        if cursor.position() < self.prompt_pos:
            cursor.setPosition(self.prompt_pos)
        self.setTextCursor(cursor)
        self.setFocus()

    def contextMenuEvent(self, event):
        # Disable context menu
        pass

    def insertPlainText(self, text):
        super().insertPlainText(text)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

    def ensure_cursor_in_allowed_area(self):
        cursor = self.textCursor()
        if cursor.position() < self.prompt_pos:
            cursor.setPosition(self.prompt_pos)
            self.setTextCursor(cursor)

    def get_current_input(self):
        cursor = self.textCursor()
        cursor.setPosition(self.prompt_pos)
        cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        text = cursor.selectedText()
        return text.strip()
