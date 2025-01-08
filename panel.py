import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

class CryptoChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crypto Chart Viewer - TradingView")

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
                #tradingview_widget {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
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
                    "interval": "1",
                    "timezone": "Etc/UTC",
                    "theme": "dark",
                    "style": "1",
                    "locale": "en",
                    "toolbar_bg": "#000000",
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
        self.setCentralWidget(self.web_view)

        # Ustawienia okna
        self.resize(1200, 800)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.center_window()

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CryptoChart()
    main_window.show()
    sys.exit(app.exec())
