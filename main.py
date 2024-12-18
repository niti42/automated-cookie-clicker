from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint


click_duration_m = 1  # play time in minutes
click_duration_s = click_duration_m*60


# keep chrome browser open after chrome finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

try:
    url = "https://orteil.dashnet.org/experiments/cookie/"
    driver.get(url)

    end_time = time.time() + click_duration_s
    last_check_time = time.time()
    while time.time() < end_time:

        cookie = driver.find_element(By.ID, value="cookie")  # click on this
        cookie.click()

        if time.time() - last_check_time >= 5:
            money = driver.find_element(By.ID, value="money")
            money_remaining = int(money.text.strip())
            print("money remaining: ", money_remaining)

            cursor = driver.find_element(By.ID, value="buyCursor")
            cursor_cost = int(cursor.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            grandma = driver.find_element(By.ID, value="buyGrandma")
            grandma_cost = int(grandma.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            factory = driver.find_element(By.ID, value="buyFactory")
            factory_cost = int(factory.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            mine = driver.find_element(By.ID, value="buyMine")
            mine_cost = int(mine.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            shipment = driver.find_element(By.ID, value="buyShipment")
            shipment_cost = int(shipment.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
            alchemyLab_cost = int(alchemy_lab.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            portal = driver.find_element(By.ID, value="buyPortal")
            portal_cost = int(portal.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            time_machine = driver.find_element(By.ID, value="buyTime machine")
            timeMachine_cost = int(time_machine.text.split(
                "-")[1].split("\n")[0].strip().replace(",", ""))

            store = {
                "cursor": (cursor_cost, cursor),
                "grandma": (grandma_cost, grandma),
                "factory": (factory_cost, factory),
                "mine": (mine_cost, mine),
                "shipment": (shipment_cost, shipment),
                "alchemyLab": (alchemyLab_cost, alchemy_lab),
                "portal": (portal_cost, portal),
                "time_machine": (timeMachine_cost, time_machine)
            }

            can_buy = {}
            for item, item_data in store.items():
                cost = item_data[0]
                if money_remaining >= cost:
                    can_buy[item] = item_data

            can_buy = dict(
                sorted(can_buy.items(), key=lambda item_data: item_data[1][0], reverse=True))

            purchase_item_data = list(can_buy.values())[0]
            purchase_item_data[1].click()  # click on the item to purchase
            print(
                f"purchased_item: {list(can_buy.keys())[0]} at {purchase_item_data[0]}")

            last_check_time = time.time()
finally:
    cookies_per_sec = driver.find_element(By.ID, value="cps")
    print("Stop Play! Let's check final score")
    print(cookies_per_sec.text)
    driver.quit()
