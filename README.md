# RPA - Robotic Process Automation Library

The RPA Library is a Selenium-based automation tool designed to simplify and streamline repetitive tasks on the web.

  

# Key Features

## WebElement

The WebElement class encapsulates web elements, allowing interactions and information extraction. Some of the methods include:

  

**inner_text()**: Returns the inner text of the element.

**get_attribute(attr)**: Returns the value of an attribute of the element.

**query_selector_all(selector)**: Locates all elements matching the specified CSS selector.

**query_selector(selector)**: Locates the first element matching the specified CSS selector.

**click()**: Simulates a click on the element.

## Browser

The Browser class manages an instance of the Chrome browser and provides methods for navigation and interaction with web elements. Some of the methods include:

  

**navigate_to(url)**: Navigates to the specified URL.

**wait_for_navigation(timeout)**: Waits until the page is fully loaded.

**wait_for_element_located(selector, type_, timeout)**: Waits until an element is present in the DOM.

**wait_for_element_visible(selector, type_, timeout)**: Waits until an element is visible on the page.

**query_selector(selector)**: Locates the first element matching the specified CSS selector.

**query_selector_all(selector)**: Locates all elements matching the specified CSS selector.

**close()**: Closes the browser.

## Tools

The Tools class provides utility methods for various tasks, such as:

  

to_csv(name, header, rows_to_save, path, delimiter): Saves data to a CSV file.

is_expired(date): Checks if a date is expired.

# Installation

* Clone this repository to your local environment.

* Ensure you have Python and Selenium installed.

## How to Use

```python
from RPA import Browser, Tools
from time import sleep

# Initialize the browser
browser = Browser(
    "user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
)

# Navigate to the RPA challenge page
browser.navigate_to("https://rpachallengeocr.azurewebsites.net/")

# Wait for an element to be visible on the page
browser.wait_for_element_visible("#tableSandbox_paginate > span")

data = []
qtd_pages = len(browser.query_selector_all("#tableSandbox_paginate > span > a"))
while qtd_pages:
    for tr in browser.query_selector_all("table#tableSandbox > tbody > tr"):
        aux = []

        td_list = tr.query_selector_all(":scope > td")
        if not Tools.is_expired(td_list[2].inner_text()):
            for td in td_list[1:-1]:
                aux.append(td.inner_text())
            aux.append(td_list[-1].query_selector(":scope > a").get_attribute("href"))
            data.append(aux)

    browser.query_selector("#tableSandbox_next").click()
    sleep(1)
    qtd_pages -= 1

# Close the browser
browser.close()

# Save the data to a CSV file
Tools.to_csv("data.csv", header=["ID", "Due Date", "Invoice URL"], rows_to_save=data)
```