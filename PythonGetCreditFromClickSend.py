from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys, os, time

textClickSend = "On the ClickSend account: "
loginClickSend = "<login>"
passwordClickSend = "<password>"
urlClickSend = "https://dashboard.clicksend.com"

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

  username = browser.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/div[1]/input")
  username.clear()
  username.send_keys(flogin)

  password = browser.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/div[2]/div[2]/input")
  password.clear()
  password.send_keys(fpass)

  browser.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/button").click()

  #Sleep before load dashboard page
  time.sleep(10)

  credit = browser.find_element_by_xpath("//div[3]/ul/li[1]/a/span/strong")
  print(fnamePortal + credit.text)

  browser.close()
  browser.quit()


getCredit(textClickSend, loginClickSend, passwordClickSend, urlClickSend)
