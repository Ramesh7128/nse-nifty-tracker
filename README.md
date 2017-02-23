# nse-nifty-tracker

A simple web app built using Cherrypy to track nse and display the top gainers table.

### Installation:

#### Install firefox version 46. Selenium is not compatible with the latest version of firefox: 
		http://	www.askmetutorials.com/2016/04/install-firefox-46-on-ubuntu-1604-1404.html

#### Install the following packages from the package manager. 
		Its a requirement for pyvirtualdisplay which allows us to run the browser in headless mode.
    	cmd: sudo apt-get install xvfb xserver-xephyr

#### Install redis server.
		https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis

#### Install python pacages
    	pip install -r requirements.txt


### Local Deployment
		Run the below command from the root directory where supervisord.conf file is present
		cmd: supervisord -c supervisord.conf
	
	
