import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QSizePolicy, QLineEdit
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
        self.tradingview_html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <style>
                body {
                    margin: 0;
                    padding: 0;
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
        self.web_view.setHtml(self.tradingview_html)

        # Create buttons for AI analysis, refreshing the chart, and changing the chart symbol
        self.analysis_button = QPushButton("Analyze Chart")
        self.refresh_button = QPushButton("Refresh Chart")
        self.change_symbol_button = QPushButton("Change Symbol")

        # Set styles for the buttons
        button_style = """
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
        """
        self.analysis_button.setStyleSheet(button_style)
        self.refresh_button.setStyleSheet(button_style)
        self.change_symbol_button.setStyleSheet(button_style)

        # Connect the buttons to their respective functions
        self.analysis_button.clicked.connect(self.run_analysis_ai)
        self.refresh_button.clicked.connect(self.refresh_chart)
        self.change_symbol_button.clicked.connect(self.change_symbol)

        # Create an input field for changing the chart symbol
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("Enter symbol (e.g., BINANCE:BTCUSDT)")
        self.symbol_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
                height: 40px;
                width: 250px;
            }
        """)

        # Set up the layout for the chart and the buttons
        main_layout = QVBoxLayout()
        chart_layout = QHBoxLayout()
        chart_layout.addWidget(self.web_view)
        main_layout.addLayout(chart_layout)

        # Add the buttons and input field below the chart
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        button_layout.addWidget(self.analysis_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.symbol_input)
        button_layout.addWidget(self.change_symbol_button)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Ustawienia okna
        self.resize(1200 * 1.1, 800 * 1.1)  # Powiększenie okna o 10%
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.center_window()

    def run_analysis_ai(self):
        # Placeholder function for AI analysis
        print("Running AI analysis...")

    def refresh_chart(self):
        # Refresh the TradingView widget
        self.web_view.setHtml(self.tradingview_html)
        print("Chart refreshed.")

    def change_symbol(self):
        # Change the symbol in the TradingView widget
        new_symbol = self.symbol_input.text()
        if new_symbol:
            self.tradingview_html = self.tradingview_html.replace(
                '"symbol": "BINANCE:BTCUSDT"',
                f'"symbol": "{new_symbol}"'
            )
            self.web_view.setHtml(self.tradingview_html)
            print(f"Symbol changed to {new_symbol}.")

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoChart()
    window.show()
    sys.exit(app.exec())
