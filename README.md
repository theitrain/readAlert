# readAlert
A flexible Python script that alerts you when a website has been updated via SMS using Twilio

### Requirements
Beautiful Soup
```
pip install beautifulsoup4
```

Twilio
```
pip install twilio
```

### Usage
You will need to have a Twilio account set up (a trial account will do for testing). If you're not familiar with Beautiful Soup and accessing parts of the dom, check out their documentation.

[Beautiful Soup Docs](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


[Twilio Docs](https://www.twilio.com/api/)

To use the script from the command line:

```
python readAlert.py
```

### Adapting
You can easily adapt this script to scrape any site and send custom text messages.  This version keeps a crude log in a text file but expanding it to use a database would not take long if that fits your needs.