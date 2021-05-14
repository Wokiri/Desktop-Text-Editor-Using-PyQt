'''
File Name: newfrontier_text_editor.py
Author: wokirijoe@gmail.com
Date: 13/05/2021

This python code creates a simple text editor with the ability to:
    1. Open existing file for editing
    2. Create a new file
    3. Save an existing edited file
    4. Save As functionality
    5. Open the following file types: ".txt", ".py",".php"

Libraries used:
    1. PyQt5 version 5.15.4
    2. python version 3.8.6
'''

# This module provides access to some variables used by python interpreter.
import sys


from PyQt5 import QtWidgets
# QtWidgets module contains various classes that are the primary elements for creating user interfaces in Qt.
# They include PYQT5 QAction, QMainWindow, QApplication, QTextEdit, QFileDialog, QDialog


from PyQt5 import QtGui, QtCore

# Subclass QMainWindow to customise your application's main window
class MainWindow(QtWidgets.QMainWindow):
    """Text Editor Mainwindow."""

    

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # initialize main window for the text editor, set geometry and title

        self.setGeometry(100,100,800,600)
        self.setWindowTitle("New Frontier Editor")

        self.appendActions()
        self.textAreaGui()

        self.filename = None


    def _createEditorActions(self):
        
        # Various FILE options
        self.new_fileAction = QtWidgets.QAction("&New",self)
        self.new_fileAction.setShortcut("Ctrl+N")
        self.new_fileAction.setStatusTip("Create a new file")
        self.new_fileAction.triggered.connect(self.new)

        self.open_fileAction = QtWidgets.QAction("&Open...",self)
        self.open_fileAction.setStatusTip("Open an existing file")
        self.open_fileAction.setShortcut("Ctrl+O")
        self.open_fileAction.triggered.connect(self.open)

        self.save_fileAction = QtWidgets.QAction("&Save",self)
        self.save_fileAction.setStatusTip("Save file")
        self.save_fileAction.setShortcut("Ctrl+S")
        self.save_fileAction.triggered.connect(self.save)

        self.cut_fileAction = QtWidgets.QAction("Cut",self)
        self.cut_fileAction.setStatusTip("Delete and copy text to clipboard")
        self.cut_fileAction.setShortcut("Ctrl+X")
        self.cut_fileAction.triggered.connect(self.textAreaGui)

        self.copy_fileAction = QtWidgets.QAction("Copy",self)
        self.copy_fileAction.setStatusTip("Copy text to clipboard")
        self.copy_fileAction.setShortcut("Ctrl+C")
        self.copy_fileAction.triggered.connect(self.textAreaGui)

        self.paste_fileAction = QtWidgets.QAction("Paste",self)
        self.paste_fileAction.setStatusTip("Paste text from clipboard")
        self.paste_fileAction.setShortcut("Ctrl+V")
        self.paste_fileAction.triggered.connect(self.textAreaGui)

        return {
            'new_fileAction':self.new_fileAction,
            'open_fileAction':self.open_fileAction,
            'save_fileAction':self.save_fileAction,
            'cut_fileAction':self.cut_fileAction,
            'copy_fileAction':self.copy_fileAction,
            'paste_fileAction':self.paste_fileAction,
        }


    
    # Appending actions to the labeled widgets
    def appendActions(self):
        self.file_Toolbar = self.addToolBar("File")
        self.file_Toolbar.addAction(self._createEditorActions()['new_fileAction'])
        self.file_Toolbar.addAction(self._createEditorActions()['open_fileAction'])
        self.file_Toolbar.addAction(self._createEditorActions()['save_fileAction'])


        self.file_Toolbar = self.addToolBar("Edit")
        self.file_Toolbar.addAction(self._createEditorActions()['cut_fileAction'])
        self.file_Toolbar.addAction(self._createEditorActions()['copy_fileAction'])
        self.file_Toolbar.addAction(self._createEditorActions()['paste_fileAction'])


    
    # Respective Labels for the File, Edit, Search options
    def textAreaGui(self):
        self.text = QtWidgets.QTextEdit(self)


        font = QtGui.QFont('Terminus', 15, QtGui.QFont.Light)
        self.text.setFont(QtGui.QFont(font))

        # Add 4 spaces everytime the tab button is pressed
        self.text.setTabStopDistance(QtGui.QFontMetricsF(self.text.font()).horizontalAdvance(' ') * 4)

        # Adjust the position from a default top-left to the GUI center
        self.setCentralWidget(self.text)

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # If the cursor position changes, call the function that displays the line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)

        return self.text


    def new(self):
        spawn = MainWindow(self)
        spawn.show()



    # Function for displaying cursor position
    def cursorPosition(self):
        cursor = self.text.textCursor()
        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))



    # Function for opening new file
    def open(self):
        filter_options = "python (*.py);; text (*.txt);; php (*.php)"
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, caption="Select file", filter=filter_options)[0]
        
        
        if self.filename:
            # if filename is a valid path to file, open for reading text
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def save(self):
        # Only open dialog if there is no filename yet
        if not self.filename:
          self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]

        if self.filename:
            # Save the contents of the text file
            with open(self.filename,"wt") as file:
                file.write(self.text.toHtml())

            self.changesSaved = True






# Function to execute the pyqt code app
def main():

    # The app is initialized with QApplication at the beginning of code execution
    # A single QApplication instance is a requirement for every application
    # The QApplication object also deals with common command line arguments hence the reason we pass sys.argv
    app = QtWidgets.QApplication(sys.argv)

    # main is an instance of the MainWindow class which inherits from QtWidgets.QMainWindow class
    main = MainWindow()

    # Show the GUI
    main.show()

    # Countinously runs Run the event loop until the parent container is closed
    sys.exit(app.exec_())


# Call main function if file is module is main
if __name__ == "__main__":
    main()
