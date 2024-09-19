
# Cookie Clicker Automation with Selenium

This project automates the popular Cookie Clicker game using Python's Selenium library. The bot clicks the cookie and buys the available upgrades (addons) when they become available, enhancing the game's progress.

## Project Structure

- **main.py**: The main script that runs the Cookie Clicker automation.
- **addons_buy()**: Function that automates the purchase of available addons every 5 seconds.
- **Game Loop**: Automates cookie clicking and manages the interval to check for available upgrades.

## Setup

1. Clone this repository.
2. Ensure that Python 3.x is installed on your machine.
3. Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

The project primarily uses the following libraries:
- `selenium`: Web automation.
- `webdriver_manager`: Automatically manages the Chrome WebDriver.

## Usage

To run the automation:

1. Ensure that you have Google Chrome installed.
2. Run the `main.py` script:

```bash
python main.py
```

The bot will automatically start clicking the cookie and purchasing the upgrades as they become available.

## Troubleshooting

- If you encounter issues related to element identification (like `NoSuchElementException` or `StaleElementReferenceException`), make sure that the game elements are correctly loaded and check the network connection.

## Known Issues

- Sometimes, the script may try to purchase an addon that is not yet available due to timing issues. The script handles this by catching the exceptions and continuing the game.
- The game may require a higher level of efficiency or error handling when it comes to rapid upgrades.

## Future Improvements

- **Upgrade Prioritization**: Add logic to prioritize purchasing specific upgrades based on their benefits.
- **Performance Metrics**: Add a feature to display the current cookies per second after a certain amount of time.
- **Error Handling**: Improve error handling for better stability.

## License

This project is licensed under the MIT License.
