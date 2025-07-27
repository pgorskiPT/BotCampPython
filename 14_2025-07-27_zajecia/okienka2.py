import sys
from PySide6.QtWidgets import QApplication, QWidget, QStyleFactory,QLineEdit, QLabel,QPushButton, QVBoxLayout

if __name__ == "__main__":
    def show_text():
        label.setText(textbox.text())

    app =QApplication(sys.argv)

    print("Style dostepne", QStyleFactory.keys())

    app.setStyle(QStyleFactory.create("windows11"))
    dialog=QWidget()
    dialog.setWindowTitle("Okno z polem tekstowym")
    dialog.setGeometry(100,100,300,150)


    textbox=QLineEdit()
    textbox.setPlaceholderText("Wpisz tu cos    ")


    label=QLabel("Tekst pojawi sie tutaj")

    button=QPushButton("Wyswietl tekst")

    button.clicked.connect(show_text)

    textbox.returnPressed.connect(show_text)

    layout=QVBoxLayout()

    layout.addWidget(textbox)
    layout.addWidget(button)
    layout.addWidget(label)

    dialog.setLayout(layout)
    dialog.show()
    sys.exit(app.exec()) # odpowiada za podtrzymanie widocznosci okienka bez komendy od razu sie zamyka
