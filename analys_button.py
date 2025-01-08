from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from panel import CryptoChart

class AnalysisButtonApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Chart Analysis")

        # Create a CryptoChart instance
        self.crypto_chart = CryptoChart()

        # Create a button
        self.button = QPushButton("Show Chart")
        self.button.setStyleSheet("background-color: green; color: white; font-size: 16px; padding: 10px;")

        # Connect the button to a function
        self.button.clicked.connect(self.show_chart)

        # Set up the layout
        layout = QHBoxLayout()
        layout.addWidget(self.crypto_chart.web_view)
        layout.addWidget(self.button)

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
    app = QApplication([])
    main_window = AnalysisButtonApp()
    main_window.show()
    app.exec()