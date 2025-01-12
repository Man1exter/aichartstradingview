# Crypto Chart Viewer - TradingView

Crypto Chart Viewer is a desktop application that allows you to view and analyze cryptocurrency charts using the TradingView widget. The application provides various functionalities such as AI analysis, refreshing the chart, changing the chart symbol, saving the chart, drawing AI suggestions, and exporting data.

## Features

- **View Cryptocurrency Charts**: Display cryptocurrency charts using the TradingView widget.
- **AI Analysis**: Analyze charts using artificial intelligence (placeholder function).
- **Refresh Chart**: Refresh the current chart.
- **Change Symbol**: Change the symbol of the chart to view different cryptocurrencies.
- **Save Chart**: Save the current chart as an image.
- **Draw AI Suggestions**: Draw suggestions on the chart using artificial intelligence.
- **Toggle AI Suggestions**: Enable or disable AI suggestions.
- **Add Alert**: Add price alerts for specific symbols.
- **Export Data**: Export chart data to a CSV file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/aichartstradingview.git
    ```
2. Navigate to the project directory:
    ```sh
    cd aichartstradingview
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Dependencies

The following dependencies are required to run the application:

- **PySide6**: `pip install PySide6`
- **Pillow**: `pip install Pillow`
- **Matplotlib**: `pip install matplotlib`
- **Requests**: `pip install requests`

You can install all dependencies at once using the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

## Configuration

Before running the application, you may need to configure certain settings. These settings can be found in the `config.json` file in the project directory. Below is an example configuration:

```json
{
    "default_symbol": "BTCUSD",
    "refresh_interval": 60,
    "ai_analysis_enabled": true
}
```

- **default_symbol**: The default cryptocurrency symbol to display.
- **refresh_interval**: The interval (in seconds) at which the chart should refresh.
- **ai_analysis_enabled**: Enable or disable AI analysis by default.

## Usage

1. Run the application:
    ```sh
    python panel.py
    ```
2. Use the buttons to interact with the chart:
    - **Analyze Chart**: Run AI analysis on the chart.
    - **Refresh Chart**: Refresh the current chart.
    - **Change Symbol**: Enter a new symbol in the input field and click "Change Symbol" to view a different cryptocurrency chart.
    - **Save Chart**: Save the current chart as an image.
    - **Draw Suggestions**: Draw AI suggestions on the chart.
    - **AI On/Off**: Toggle AI suggestions on or off.
    - **Add Alert**: Add price alerts for specific symbols.
    - **Export Data**: Export the current chart data to a CSV file.

## Troubleshooting

If you encounter any issues while using the application, here are some common solutions:

- **Application not starting**: Ensure that all dependencies are installed correctly by running `pip install -r requirements.txt`.
- **Chart not loading**: Check your internet connection and ensure that the TradingView widget is accessible.
- **AI analysis not working**: Verify that the AI analysis feature is enabled in the `config.json` file.
- **Export data not working**: Ensure that you have write permissions to the directory where the CSV file is being saved.

If the issue persists, please open an issue on the GitHub repository.

## FAQ

**Q: How do I change the default symbol?**
A: You can change the default symbol by editing the `default_symbol` field in the `config.json` file.

**Q: Can I disable AI analysis?**
A: Yes, you can disable AI analysis by setting the `ai_analysis_enabled` field to `false` in the `config.json` file.

**Q: How do I export chart data?**
A: Click the "Export Data" button to save the current chart data to a CSV file.

**Q: Where can I report bugs or request features?**
A: You can report bugs or request features by opening an issue on the GitHub repository.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [TradingView](https://www.tradingview.com/) for providing the chart widget.
- [PySide6](https://pypi.org/project/PySide6/) for the GUI framework.
- [Pillow](https://pypi.org/project/Pillow/) for image processing.
- [Matplotlib](https://matplotlib.org/) for plotting charts.

## Contact

For further inquiries, please contact us at support@yourdomain.com.

## Changelog

### v1.1.0
- Added "Export Data" feature to export chart data to a CSV file.
- Added "Configuration" section to the README.
- Added "Troubleshooting" section to the README.
- Added "FAQ" section to the README.
- Added "Contact" section to the README.

### v1.0.0
- Initial release of Crypto Chart Viewer.
- Features: View cryptocurrency charts, AI analysis, refresh chart, change symbol, save chart, draw AI suggestions, toggle AI suggestions, add alert.

## Credits

- **Contributors**: Thanks to all the contributors who have helped improve this project.
- **Third-Party Libraries**: This project uses the following third-party libraries:
  - [TradingView](https://www.tradingview.com/)
  - [PySide6](https://pypi.org/project/PySide6/)
  - [Pillow](https://pypi.org/project/Pillow/)
  - [Matplotlib](https://matplotlib.org/)

## Support

If you need help or support, you can:

- Visit our [GitHub Discussions](https://github.com/yourusername/aichartstradingview/discussions) page to ask questions and get help from the community.
- Check the [FAQ](#faq) section for answers to common questions.
- Contact us directly at support@yourdomain.com for further assistance.