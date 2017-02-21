from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import urlparse

display = Display(visible=1)
display.start()
prof = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile = prof)
driver.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G')
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="topGainers")
rows = table.findAll(lambda tag: tag.name=='tr')
for tr in rows:
	cols = tr.findAll('td')
	for td in cols:
		print td.find(text=True)
	print "new row"

driver.quit()
display.stop()


