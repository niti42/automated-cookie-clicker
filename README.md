# Cookie Clicker Automation Script

This script automates gameplay for the Cookie Clicker game available at [Cookie Clicker Experiment](https://orteil.dashnet.org/experiments/cookie/). It uses Selenium to interact with the game, continuously clicking the cookie and purchasing the most cost-efficient upgrades.

## Features

- Automates cookie clicking for a specified duration.
- Automatically purchases upgrades (e.g., cursors, grandmas, factories) when enough cookies are available.
- Prioritizes upgrades based on cost-efficiency.

## Prerequisites

1. Python 3.x installed on your system.
2. Google Chrome browser installed.
3. ChromeDriver compatible with your Chrome version. You can download it [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Installation

1. Clone this repository or copy the script.
2. Install the required Python packages:
   ```
   pip install selenium
   ```
3. Place the chromedriver executable in a directory included in your system's PATH or in the same directory as the script.

## Usage

1. Update the click_duration_m variable in the script to set the duration (in minutes) for which the bot should play.
2. Run the script:

```
python cookie_clicker_bot.py
```

3. The bot will open a Chrome browser, start clicking the cookie, and automatically buy upgrades as funds allow.

## How It Works

- The script starts by opening the Cookie Clicker game in a Chrome browser.
- It continuously clicks the cookie element to generate cookies.
- Every 5 seconds, it checks available money and compares it with the cost of upgrades.
- It buys the most expensive upgrade that can be afforded at the moment, prioritizing efficiency.

## Code Highlights

- Selenium WebDriver: Used for browser automation.
- Upgrade Purchasing Logic: A dictionary of store items is created, sorted by cost, and the most expensive affordable item is purchased.
- Exception Handling: Ensures the browser is properly closed at the end of execution.

## Customization

- Adjust the click_duration_m variable to change the play duration.
- Modify the upgrade priority logic by altering the store dictionary sorting criteria.

## Notes

- The script keeps the browser open for debugging purposes. To close it automatically, remove the detach option in the ChromeOptions.
- Ensure that the website's structure hasn't changed, as the script relies on specific element IDs.

## Disclaimer

- This script is for educational and personal use only. Using automation tools on websites without permission may violate their terms of service.
