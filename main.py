import RPA
from RPA.tools import Tools
from time import sleep

browser = RPA.Browser(
    "user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
    # "--headless=true"
)

browser.navigate_to("https://rpachallengeocr.azurewebsites.net/")
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
    qtd_pages-=1

browser.close()


Tools.to_csv("data.csv", header=["ID", "Due Date", "Invoice URL"], rows_to_save=data)