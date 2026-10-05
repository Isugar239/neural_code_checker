import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("ОтличийНет")
    window.resize(800, 500)
    window.setCentralWidget(QLabel("Здесь будет окно сравнения"))
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
