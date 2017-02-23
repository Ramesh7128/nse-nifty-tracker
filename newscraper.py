from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

# launch stuff inside virtual display here
browser = webdriver.Firefox()
browser.get('http://www.google.com')
print browser.title
browser.quit()
vdisplay.stop()