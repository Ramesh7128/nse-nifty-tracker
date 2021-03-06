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
import redis
import time

r = redis.Redis(host='localhost', port=6379)
starttime=time.time()


def nse_data_scraper():
	"""
	scraper function which gets called every 5 mins
	"""
	try:
		prof = webdriver.FirefoxProfile()
		display = Display(visible=0, size=(1024, 768))
		display.start()
		driver = webdriver.Firefox(firefox_profile = prof)
		driver.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G')
		page_source = driver.page_source
		soup = BeautifulSoup(page_source, 'html.parser')
		table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="topGainers")
		rows = table.findAll(lambda tag: tag.name=='tr')
		heading = []
		for tr in rows:
			headers = tr.findAll('th')
			for th in headers:
				heading.append(th['title'])

		for row_index in range(len(rows)):
			cols = rows[row_index].findAll('td')
			stock = {}
			for col_index in range(len(cols)):
				stock[heading[col_index]] = cols[col_index].find(text=True)
			try:
				print stock
				float(stock['% Change'])
				r.hmset("stock:%s" % str(row_index), stock)
			except Exception as e:
				#log errors
				pass
	except Exception, e:
		# log errors
		pass
	finally:
		driver.quit()
		display.stop()

if __name__ == "__main__":
	while True:
		nse_data_scraper()
		time.sleep(300.0 - ((time.time() - starttime) % 60.0))



