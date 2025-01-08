import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

class CryptoChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Chart Viewer - TradingView")

        # Ustawienia ogólne okna (czarne tło)
        self.setStyleSheet("background-color: black;")  # Ustawienie czarnego tła dla całej aplikacji

        # Widget WebEngineView do wyświetlenia widgetu TradingView
        self.web_view = QWebEngineView()

        # HTML osadzonego widgetu TradingView
        tradingview_html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <style>
                body {
                    margin: 0;
                    background-color: black;
                    height: 100%;
                    overflow: hidden;
                }
            </style>
        </head>
        <body>
            <div id="tradingview_widget"></div>
            <script type="text/javascript">
                new TradingView.widget({
                    "width": "100%",
                    "height": "100%",
                    "symbol": "BINANCE:BTCUSDT",
                    "interval": "D",
                    "timezone": "Etc/UTC",
                    "theme": "dark",
                    "style": "1",
                    "locale": "en",
                    "toolbar_bg": "#f1f3f6",
                    "enable_publishing": false,
                    "allow_symbol_change": true,
                    "container_id": "tradingview_widget"
                });
            </script>
        </body>
        </html>
        '''

        # Załaduj HTML do WebEngineView
        self.web_view.setHtml(tradingview_html)

        # Create a button for AI analysis
        self.analysis_button = QPushButton("Analiza AI")
        self.analysis_button.setStyleSheet("""
            background-color: #28a745;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            height: 40px;
            width: 150px;
        """)

        # Efekt najechania na przycisk
        self.analysis_button.setStyleSheet("""
            background-color: #28a745;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            height: 40px;
            width: 150px;
        """)
        self.analysis_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                height: 40px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #218838;  # Darker green on hover
            }
            QPushButton:pressed {
                background-color: #1e7e34;  # Even darker green on press
            }
        """)

        # Connect the button to a function
        self.analysis_button.clicked.connect(self.run_analysis_ai)

        # Set up the layout for both the chart and the button
        main_layout = QVBoxLayout()  # Zmieniono z QHBoxLayout na QVBoxLayout
        chart_layout = QHBoxLayout()
        chart_layout.addWidget(self.web_view)
        main_layout.addLayout(chart_layout)

        # Add the analysis button below the chart
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Spacer, aby przycisk był z prawej
        button_layout.addWidget(self.analysis_button)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Ustawienia okna
        self.resize(1200 * 1.1, 800 * 1.1)  # Powiększenie okna o 10%
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.center_window()

        # Uruchomienie analysis_button.py automatycznie
        subprocess.run([sys.executable, 'analysis_button.py'])

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def run_analysis_ai(self):
        """Funkcja uruchamiająca analizę AI (można dostosować w zależności od wymagań)."""
        print("Uruchamianie analizy AI...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CryptoChart()
    main_window.show()
    sys.exit(app.exec())




