import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

class CryptoChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Chart Viewer - TradingView")
        self.setGeometry(100, 100, 1200, 800)

        # Widget WebEngineView do wyświetlenia widgetu TradingView
        self.web_view = QWebEngineView()

        # HTML osadzonego widgetu TradingView
        tradingview_html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        </head>
        <body>
            <div id="tradingview_widget"></div>
            <script type="text/javascript">
                new TradingView.widget({
                    "width": 1100,
                    "height": 700,
                    "symbol": "BINANCE:BTCUSDT",
                    "interval": "1",
                    "timezone": "Etc/UTC",
                    "theme": "dark",
                    "style": "1",
                    "locale": "en",
                    "toolbar_bg": "#f1f3f6",
                    "enable_publishing": false,
                    "hide_top_toolbar": true,
                    "save_image": false,
                    "container_id": "tradingview_widget"
                });
            </script>
        </body>
        </html>
        '''

        # Załaduj HTML do WebEngineView
        self.web_view.setHtml(tradingview_html)

        # Ustawienia układu
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CryptoChart()
    main_window.show()
    sys.exit(app.exec())