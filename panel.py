import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests
from io import BytesIO
from PIL import Image

# Funkcja do pobierania danych z TradingView
# TradingView nie udostępnia oficjalnego API dla publicznego użytku, więc korzystamy z alternatywnych źródeł danych
# (np. Binance lub CoinGecko do pobierania wykresu lub danych)
def fetch_chart(pair="BTCUSDT"):
    # Przykladowy link do wykresu TradingView (można zastąpić własnym źródłem danych)
    chart_url = f"https://s3.tradingview.com/snapshots/o/O{pair}.png"  # Przykład (dla ilustracji)

    try:
        response = requests.get(chart_url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            raise Exception("Nie udało się pobrać wykresu. Kod błędu: " + str(response.status_code))
    except Exception as e:
        print(f"Błąd: {e}")
        return None

# Główna klasa aplikacji
def create_main_window():
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Crypto Chart Viewer")
            self.setGeometry(100, 100, 800, 600)

            # Layout
            layout = QVBoxLayout()

            # Label na wykres
            self.chart_label = QLabel("Pobieranie wykresu...")
            self.chart_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.chart_label)

            # Główne okno
            container = QWidget()
            container.setLayout(layout)
            self.setCentralWidget(container)

            # Załaduj wykres
            self.load_chart("BTCUSDT")

        def load_chart(self, pair):
            image = fetch_chart(pair)
            if image:
                # Konwersja obrazu PIL na QPixmap
                qimage = ImageQt.toqpixmap(image.convert("RGBA"))
                pixmap = QPixmap.fromImage(qimage)
                self.chart_label.setPixmap(pixmap)
            else:
                self.chart_label.setText("Nie udało się załadować wykresu.")

    return MainWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = create_main_window()
    main_window.show()
    sys.exit(app.exec())