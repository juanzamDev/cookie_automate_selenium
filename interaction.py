from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver with headless option
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open a web browser and navigate to the Wikipedia main page
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    # Find the element containing the article count
    article_count_element = driver.find_element(By.ID, "articlecount")

    # Extract the text and print it
    article_count = article_count_element.find_element(By.TAG_NAME, "a").text
    print(f"Número de artículos en Wikipedia: {article_count}")

finally:
    # Close the browser
    driver.quit()