from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

service = Service("/usr/local/Cellar/geckodriver/0.30.0/bin/geckodriver")

driver = Firefox(service=service)

driver.get("https://selenium.dev")

driver.quit()