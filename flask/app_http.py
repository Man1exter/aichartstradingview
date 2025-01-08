from flask import Flask, render_template_string
import threading

app = Flask(__name__)

@app.route('/')
def index():
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
    return render_template_string(tradingview_html)

def run_flask_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()
