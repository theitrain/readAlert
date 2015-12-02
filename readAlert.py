import twilio
import requests
import bs4
import secrets

URL = 'http://www.google.com/'
MESSAGE = 'Google updated their doodle!'


def main():

    f = open('log.txt', 'r')
    current = f.readlines()
    f.close()

    if (scrapeSite(URL, current) is True):
        sendAlert()


def scrapeSite(url, current):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    logo = soup.select('#hplogo')
    logo = logo[0]

    if logo['src'] != current:
        f = open('log.txt', 'w')
        f.write(logo['src'])
        return True

    return False


def sendAlert():
    try:
        client = twilio.rest.TwilioRestClient(secrets.TWILIO_ID, secrets.TWILIO_TOKEN)
        message = client.messages.create(
            body=MESSAGE,
            to=secrets.RECIPIENT_NUMBER,
            from_=secrets.TWILIO_NUMBER
            )
        print('Success! message ID: ' + message.sid)

    except twilio.TwilioRestException as e:
        print(e)

if __name__ == "__main__": main()
