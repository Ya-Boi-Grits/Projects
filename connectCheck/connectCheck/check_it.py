# A library designed for working with urls. [.request] specified to work with the response
import urllib.request as urllib


def initialized(url):
    response = urllib.urlopen(url)  # Opens the url
    code = response.getcode()  # Grabs the response code
    if code == 200:
        return print(f"Connection to {url} was successful")
    else:
        return print(f"Could not connect to {url}. Code {code}")


# Simple function call
initialized("https://www.google.com/")
