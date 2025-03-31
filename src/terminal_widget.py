# terminal_widget.py
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QTextCursor

class TerminalWidget(QTextEdit):
    input_submitted = pyqtSignal(str)

    def __init__(UwU, parent=None):
        super().__init__(parent)
        UwU.standard_prompt = "(´• ω •`)>"
        UwU.prompt = UwU.standard_prompt
        UwU.expecting_input = False
        UwU.prompt_pos = 0  # Position in the document where the prompt ends
        UwU.init_terminal()
        UwU.cursorPositionChanged.connect(UwU.ensure_cursor_in_allowed_area)

    def init_terminal(UwU):
        UwU.setReadOnly(False)
        UwU.set_prompt(UwU.prompt)

    def set_prompt(UwU, prompt_text):
        UwU.prompt = prompt_text
        UwU.moveCursor(QTextCursor.End)
        if not UwU.toPlainText().endswith('\n'):
            UwU.insertPlainText('\n')
        UwU.insertPlainText(UwU.prompt)
        UwU.moveCursor(QTextCursor.End)
        # Update prompt position to after the prompt
        UwU.prompt_pos = UwU.textCursor().position()
        UwU.ensureCursorVisible()

    def append_output(UwU, text):
        # Remove existing prompt if present
        cursor = UwU.textCursor()
        cursor.setPosition(UwU.prompt_pos)
        cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        if cursor.hasSelection():
            cursor.removeSelectedText()
        # Move cursor to end
        UwU.moveCursor(QTextCursor.End)
        # Insert newline if needed
        if not UwU.toPlainText().endswith('\n'):
            UwU.insertPlainText('\n')
        # Insert the output
        UwU.insertPlainText(text)
        # Update prompt position
        UwU.prompt_pos = UwU.textCursor().position()


    def keyPressEvent(UwU, event):
        cursor = UwU.textCursor()
        pos = cursor.position()

        if pos < UwU.prompt_pos:
            cursor.setPosition(UwU.prompt_pos)
            UwU.setTextCursor(cursor)

        if event.key() == Qt.Key_Backspace:
            if pos > UwU.prompt_pos:
                super().keyPressEvent(event)

        elif event.key() in (Qt.Key_Return, Qt.Key_Enter):
            if UwU.expecting_input:
                user_input = UwU.get_current_input()
                UwU.input_submitted.emit(user_input)
                UwU.expecting_input = False
            else:
                UwU.insertPlainText('\n')
                UwU.set_prompt(UwU.standard_prompt)

            UwU.moveCursor(QTextCursor.End)
            UwU.ensureCursorVisible()

        else:
            super().keyPressEvent(event)
            if cursor.position() < UwU.prompt_pos:
                cursor.setPosition(UwU.prompt_pos)
                UwU.setTextCursor(cursor)


    def mousePressEvent(UwU, event):
        cursor = UwU.cursorForPosition(event.pos())
        if cursor.position() < UwU.prompt_pos:
            cursor.setPosition(UwU.prompt_pos)
        UwU.setTextCursor(cursor)
        UwU.setFocus()

    def contextMenuEvent(UwU, event):
        # Disable context menu
        pass

    def insertPlainText(UwU, text):
        super().insertPlainText(text)
        UwU.moveCursor(QTextCursor.End)
        UwU.ensureCursorVisible()

    def ensure_cursor_in_allowed_area(UwU):
        cursor = UwU.textCursor()
        if cursor.position() < UwU.prompt_pos:
            cursor.setPosition(UwU.prompt_pos)
            UwU.setTextCursor(cursor)

    def get_current_input(UwU):
        cursor = UwU.textCursor()
        cursor.setPosition(UwU.prompt_pos)
        cursor.movePosition(QTextCursor.End, QTextCursor.KeepAnchor)
        text = cursor.selectedText()
        return text.strip()
