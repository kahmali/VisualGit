import sys

from PyQt4 import QtGui, QtCore, uic

from localrepoapi import LocalRepoApi


class TestApp(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Load and display UI file
        self.ui = uic.loadUi('/home/kahmali/Development/Projects/VisualGit/ui/mainwindow.ui')
        self.ui.show()

        # Connect testButton's clicked() signal to our testFunc() function
        self.connect(self.ui.testButton, QtCore.SIGNAL("clicked()"), testFunc)

        root_commit = LocalRepoApi.get_git_graph("/home/kahmali/Development/Projects/TestGit")


def testFunc():
    win.ui.commitMessageTextEdit.setText('Message!')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = TestApp()
    sys.exit(app.exec_())
