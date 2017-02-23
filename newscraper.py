from xvfbwrapper import Xvfb
from selenium import webdriver
vdisplay = Xvfb()
vdisplay.start()
prof = webdriver.FirefoxProfile()

# launch stuff inside virtual display here
browser = webdriver.Firefox(firefox_profile = prof)
browser.get('http://www.google.com')
print browser.title
browser.quit()
vdisplay.stop()