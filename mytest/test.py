from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

if __name__ == "__main__":
    print(2*"---"+"Hello World"+2*"---")

    driver = webdriver.Chrome(executable_path=r'C:\Chrome\chromedriver.exe')
    driver.get('http://www.google.com')
    # time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    # time.sleep(5)  # Let the user actually see something!
    driver.quit()


    print(2*"---"+"The End"+2*"---")
