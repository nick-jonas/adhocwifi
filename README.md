## Ad-hoc WiFi / Device Setup

#### To run server manually

1. ssh in as pi user (password: raspberry)
2. stop daemon service ```sudo /etc/init.d/coder-daemon stop```
3. change to coder user ```sudo su coder```
(make sure coder user has bash profile in /etc/passwd)
4. start server ```cd /home/coder/coder-dist/coder-base && /opt/node/bin/node server.js```



#### Reset Button

Hook up a momentary push button to pin 18 on the RPi's GPIO, and connect the ground.  This will reset /home/weather/config.json and /etc/wpa_supplicant/wpa_supplicant.conf

![Wiring](http://razzpisampler.oreilly.com/images/rpck_1101.png "Wiring")




## TODO

- momentary push button to reset WiFi

Put a reset.txt on the boot drive in the coder_settings folder. That'll force you through the password setting and wifi setup again.

There's also a subfolder called reset_files. Inside there is a file called wpasupplicant or something like that. That's the default wifi settings. If you don't want to reset your password, just copy this file and paste it into the coder_settings directory to update the wifi settings only.


- internet connectivity

adjust light code to ping Google every 10 seconds (for internet connection), and ping weather service every 10 minutes