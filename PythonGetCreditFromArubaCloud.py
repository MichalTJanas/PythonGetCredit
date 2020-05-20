from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys, os, time

textAruba = "On the ArubaCloud account: "
loginAruba = "<login>"
passwordAruba = "<password>"
urlAruba = "https://admin.dc5.arubacloud.pl"

chromeDriverPath = os.path.abspath("chromedriver")

chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(
  executable_path=chromeDriverPath,
  options=chrome_options
  )

def getCredit(fnamePortal, flogin, fpass, furl):
    wait = WebDriverWait(browser, 10)

    browser.get(furl)

    username = browser.find_element_by_name("ctl00$MainContent$txtAccount")
    username.clear()
    username.send_keys(flogin)

    password = browser.find_element_by_name("ctl00$MainContent$txtPassword")
    password.clear()
    password.send_keys(fpass)

    browser.find_element_by_name("ctl00$MainContent$btnValidate").click()

    #Sleep before load dashboard page
    time.sleep(10)

    credit = browser.find_element_by_id("lblTopCredit")
    creditUntil = browser.find_element_by_id("lblCostUnit")
    print(fnamePortal + credit.text + " " + creditUntil.text)

    browser.close()
    browser.quit()

getCredit(textAruba, loginAruba, passwordAruba, urlAruba)
