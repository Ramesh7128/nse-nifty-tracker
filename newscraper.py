from xvfbwrapper import Xvfb
from selenium import webdriver
vdisplay = Xvfb()
vdisplay.start()

# launch stuff inside virtual display here
browser = webdriver.PhantomJS()()
browser.get('http://www.google.com')
print browser.title
browser.quit()
vdisplay.stop()