# import urllib
# import urllib.request to get the data from the url
# write a function that takes a url
# returns a response

import urllib.request as urllib

print("This is the site checker connectivity")
site_url = input("Enter your site url to check:\n")


def main(url):
    print("Checking connection...")
