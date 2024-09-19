import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Game loop variable
active_game = True
click_counter = 0
last_addon_buy_time = time.time()
start_time = time.time()  # Track the start time of the game
addons_list = []
block_addons = []

# Function to buy addons every 5 seconds
def addons_buy(click_counter):
    global addons_list, block_addons

    # Find the elements inside the div right panel looking for available addons
    right_panel = driver.find_element(By.ID, 'rightPanel')
    available_addons = right_panel.find_elements(By.CSS_SELECTOR, 'div:not(.grayed)')  # Addons that are not grayed out

    for addon in available_addons:
        try:
            addon_id = addon.get_attribute('id')
            
            # Ensure the addon_id is valid and non-empty
            if addon_id and addon_id not in addons_list:
                # If it's not already in the addons list, add it
                addons_list.append(addon_id)
                print(f"Nuevo addon disponible: {addon_id}")

            if addon_id and addon_id not in block_addons:
                print(f"Comprando addon: {addon_id}")
                try:
                    # Try to buy the addon
                    buying_addon = driver.find_element(By.ID, addon_id)
                    buying_addon.click()
                    block_addons.append(addon_id)  # Add to block_addons after purchase
                    print(f"Addon {addon_id} comprado.")
                except NoSuchElementException:
                    print(f"No se pudo encontrar el elemento con ID {addon_id}.")
                except StaleElementReferenceException:
                    print(f"El addon {addon_id} ya no está disponible.")
                    
        except StaleElementReferenceException:
            print(f"Elemento stale encontrado para el addon {addon_id}, intentando de nuevo...")

# Open a web browser and navigate to the game
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(By.ID, 'cookie')

# Game loop
while active_game:
    cookie_button.click()

    # Check to run the function every 5 seconds
    if time.time() - last_addon_buy_time >= 5:
        addons_buy(click_counter)
        last_addon_buy_time = time.time()

    # Stop the game after 5 minutes (300 seconds)
    if time.time() - start_time >= 600:
        active_game = False  # Stop the loop after 5 minutes
        cookies_per_second = driver.find_element(By.ID, 'cps').text  # Retrieve cookies/second
        print(f"Cookies per second: {cookies_per_second}")
        break

    click_counter += 1