# RainCheck-pi

Your raspberry pi warns to get an umbrella on a rainy day. Uses [forecast.io](http://forecast.io/) to get forecast information.

To use it, get a free API key from [here](https://developer.forecast.io/) that allows for a 1000 querries per day. This will use about 48 per day. Use the remaining ones as you wish.

Clone via `git clone https://github.com/oganm/RainCheck-pi.git`

Fill the required information to `.config` file. Obama's config file would look like this
```
[forecast.io]
lattitude = 38.8977
longitude = 77.0366
apikey = presidentialKey

[piConfig]
rainlaterout = 12
rainnowout = 20
```
`rainlaterout` will be turned on if it is likely to rain anytime that day while (p>0.4) `rainnowout` will be turned on if it is raining right now.

You also need the forecast.io API wrapper by [ZeevG](https://github.com/ZeevG/python-forecast.io). Just do `pip-3.2 install python-forecastio`. pip's name might change depending on your installation method.

to run, after filling the config file, do
```
cd RainCheck-pi
chmod +x rainWarning.py
sudo ./rainWarning.py
```

# Setup
I just use a pair of LEDs as input you can find a simple tutorial [here](https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/gpio-examples-1-a-single-led/). Just don't try putting the LED directly. I find an extension board and a ribbon cable extremely helpful since it is quite easy to short circuit the pi when you bring exposed cables near the GPIO pins directly. You can look for them at ebay but make sure you are buying for the right version of pi. The more recent ones have 40 pins. Also [here's](http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/) a tutorial about naming scheme of the pins.
