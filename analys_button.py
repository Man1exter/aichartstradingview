import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from panel import CryptoChart  # Importujemy panel.py, który zawiera CryptoChart

class AnalysisButtonApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Chart Analysis")

        # Create a CryptoChart instance
        self.crypto_chart = CryptoChart()

        # Create a button
        self.button = QPushButton("Show Chart")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: green;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                height: 40px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: darkgreen;
            }
        """)

        # Connect the button to a function
        self.button.clicked.connect(self.show_chart)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.crypto_chart.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Window settings
        self.resize(1200, 800)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.center_window()

    def show_chart(self):
        self.crypto_chart.show()

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AnalysisButtonApp()
    main_window.show()
    sys.exit(app.exec())
