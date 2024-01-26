import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from pylatexenc.latex2svg import LatexNodes2SVG 

class LatexEditor(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.editor = QTextEdit()
        self.editor.textChanged.connect(self.update_preview)
        
        self.preview = QWebEngineView()
        
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.preview)
        
        self.setCentralWidget(self.splitter)
        
        self.update_preview()
        
    def update_preview(self):
       latex = self.editor.toPlainText()
       converter = LatexNodes2SVG()
       svg = converter(latex) 
       
       self.preview.setHtml(svg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LatexEditor()
    window.show()
    app.exec_()