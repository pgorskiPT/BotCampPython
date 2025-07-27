import sys
from PySide6.QtWidgets import QApplication, QWidget, QStyleFactory

if __name__ == "__main__":

    app =QApplication(sys.argv)

    print("Style dostepne", QStyleFactory.keys())


    app.setStyle(QStyleFactory.create("windows11"))
    window=QWidget()
    window.setWindowTitle("Demo z windows11 ")
    window.resize(300,200)
    window.show()


    sys.exit(app.exec())
