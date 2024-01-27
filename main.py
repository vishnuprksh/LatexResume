import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QPlainTextEdit
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt, QProcess
from latex_updater import get_newresumelatex


class LatexEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LaTeX Editor")
        self.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.editor = QPlainTextEdit()
        self.job_desc_editor = QPlainTextEdit()  # New editor for job description
        self.compile_button = QPushButton("Compile")

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.job_desc_editor)  # Add job description editor to layout
        layout.addWidget(self.compile_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect the button click event to the compile function
        self.compile_button.clicked.connect(self.compile_latex)

    def compile_latex(self):
        # Get the LaTeX code from the main editor
        latex_code = self.editor.toPlainText()

        with open("old_latex.tex", "w") as f:
            f.write(latex_code)

        # Get the job description from the job description editor
        job_desc = self.job_desc_editor.toPlainText()

        with open("job_description.txt", "w") as f:
            f.write(job_desc)

        # Get the updated LaTeX code using the get_newresumelatex function
        updated_latex_code = get_newresumelatex(latex_code, job_desc)

        # Create a temporary .tex file to store the updated LaTeX code
        with open("new_latex.tex", "w") as f:
            f.write(updated_latex_code)

        # # Run the pdflatex command to generate a PDF
        # process = QProcess()
        # process.start("pdflatex", ["new_latex.tex"])
        # process.waitForFinished()

        # Display a message indicating the PDF is generated
        print("PDF generated. Open using an external viewer.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LatexEditor()
    window.show()
    sys.exit(app.exec_())
