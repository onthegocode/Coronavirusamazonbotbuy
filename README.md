# Coronavirusamazonbotbuy

## This bot will help with the whole foods market checkout to automatically log you in and go to check out and if no options are available it will refresh page till there is an option. Also, this has some tactics to make the Recaptcha not appear like randomly writing at a different pace, changing window size, and changing the agent user every time it reboots. Also if there is an error of some sort it will reboot itself and close down the browser and start a new one up from the beginning. This is still a work in progress but it will be updated more. Hopefully someone can use this to help them get their much needed supplies. Enjoy :D

#### You will need to download python from https://www.python.org/ 
#### Also open up the bot.py script and where you see email and password just change it with your email and password, but make sure its with in the ' '
#### You also might need to pip install random, time, selenium, fake_useragent, selenium.webdriver.chrome.options modules instructions will be below

### Copy and paste into cmd once you downloaded python 

#### For random module copy --> pip install random
#### For time module copy --> pip install time
#### For selenium copy --> pip install selenium 
#### For fake_useragent --> pip install fake_useragent
#### For selenium.webdriver.chrome.options copy --> pip install selenium.webdriver.chrome.options

#### For the chrome driver you might need to go to https://chromedriver.chromium.org/downloads and download the version of chrome you have to check what version of chrome you have type this in your browser chrome://version and it should be to the right of Google Chrome: 

#### Once you download the zip file of the chrome driver extract it with winrar or any other zip extractor then replace the current chromedriver.exe in the file with your new one, make sure it's in the same file as the bot.py script because if it isn't then it won't work, since it won't be able to find the chromedriver.exe which is what opens the browser. 


### When all the steps above are complete all you have to do is go to cmd (might have to run it as admin just right click it and click run as admin) go to File Explorer (You can click file locator go to the file manually and then on the search bar type cmd and then enter and it should bring up cmd) and type python bot.py then enter and thats it :D hope you enjoy!


#### New Features
##### Added some new features one of them being the ability to save your email and password to your computer using a json file. This will allow the program to be able to run right away instead of it having to constantly ask you for your email and password. Also if you need to change your password just run the change.py script and it will ask you again for your email and password and reset it. Another thing that was added was the Fresh market option where now you can either pick fresh market or whole foods market which ever one you want! :D

### If their are any errors like a recaptcha or the screen closes or just stays at the amazon homepage, try and delete your cookies or to be safe all of your history, and just re-run the program. Sometimes the recaptcha on amazon will catch the bot even if you delete your history and everything and it can be due to screen size that the bot will change too. All you need to do is just re-run it. I am currently working on getting paste the recaptcha and figuring out what triggers it but probably won't figure it out till a while, but for now just delete your history and re-run the program until it works. If anyone can help with this issues I'll be more than happy to get it still learning about recaptchas and bots. Hopefully people get some good use out of this :D. Thank you!
