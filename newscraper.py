from pyvirtualdisplay import Display
from selenium import webdriver

xephyr=Display(visible=0, size=(320, 240))
xephyr.start()
prof = webdriver.FirefoxProfile()

# launch stuff inside virtual display here
browser = webdriver.Firefox(firefox_profile = prof)
browser.get('http://www.google.com')
print browser.title
browser.quit()
xephyr.stop()