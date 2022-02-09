from PyPDF2.generic import readHexStringFromStream
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import PyPDF2
import sapiva
import os, sys

path = ""
content = ""

class win(QMainWindow):
    def __init__(self):
        super(win, self).__init__()
        uic.loadUi("editor.ui", self)
        self.show()

        self.actionOpen.clicked.connect(self.open_doc)
        self.actionRead.clicked.connect(self.read_doc)
    
    def open_doc(self):
        op = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, 
        "Open", "C:\\", 
        "Text Documents (*.txt);;PDF (*.pdf);;All Files (*)", options=op)
        if file != "":
            with open(file, "r") as f:
                self.setWindowTitle(f"{os.path.basename(file)} - AudioPlus")

                f_e = os.path.splitext(file)

                global path
                if f_e[1] == ".pdf":
                    reader = PyPDF2.PdfFileReader(file)
                    obj = reader.getPage(0)
                    global path
                    global content
                    path = f.name
                    content = obj.extractText()
                    self.actionRead.setEnabled(True)

                    for page in range(reader.numPages):
                        bobj = reader.getPage(page)
                        self.readBox.setPlainText(bobj.extractText())
                else:
                    path = f.read()
                    self.readBox.setPlainText(path)
                    self.actionRead.setEnabled(True)
    
    def read_doc(self):
        if path != "":
            f_e = os.path.splitext(path)
            if f_e[1] == ".pdf":
                reader = PyPDF2.PdfFileReader(path)
                for page in range(reader.numPages):
                    obj = reader.getPage(page)
                    sapiva.set_rate(125)
                    sapiva.set_volume(1.0)
                    sapiva.speak(obj.extractText())
            else:
                sapiva.set_rate(125)
                sapiva.set_volume(1.0)
                sapiva.speak(path)
    
def main():
    app = QApplication([])
    window = win()
    app.exec_()

if __name__ == "__main__":
    main()