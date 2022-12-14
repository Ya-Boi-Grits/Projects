import requests
import urllib.request as urllib
# A library designed for working with urls. [.request] specified to work with the response


def initialized(url):
    response = urllib.urlopen(url)  # Opens the url
    code = response.getcode()  # Grabs the response code
    if code == 200:
        return print(f"Connection to {url} was successful. Code {code}")
    else:
        return print(f"Could not connect to {url}. Code {code}")


# Simple function call
initialized("https://www.google.com/")


# ------------- The same thing but with [requests] library instead of [urllib] ---------


def init2(url):
    request = requests.get(url)
    code = request.status_code
    if code == 200:
        return print(f"Connection to {url} was successful. Code {code}")
    else:
        return print(f"Error. Could not connect to {url}. Code {code}")


init2("https://wiki.mabinogiworld.com/view/Erg")
