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

        self.filename = None


    def _createEditorActions(self):
        
        # Various FILE options
        self.new_fileAction = QtWidgets.QAction("&New",self)


        self.open_fileAction = QtWidgets.QAction("&Open...",self)


        self.save_fileAction = QtWidgets.QAction("&Save",self)


        return {
            'new_fileAction':self.new_fileAction,
            'open_fileAction':self.open_fileAction,
            'save_fileAction':self.save_fileAction,
        }


    
    # Appending actions to the labeled widgets
    def appendActions(self):
        self.file_Toolbar = self.addToolBar("File")
        self.file_Toolbar.addAction(self._createEditorActions()['new_fileAction'])
        self.file_Toolbar.addAction(self._createEditorActions()['open_fileAction'])
        self.file_Toolbar.addAction(self._createEditorActions()['save_fileAction'])


    




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

