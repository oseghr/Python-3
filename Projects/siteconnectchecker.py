# import urllib
import urllib.request as urllib

print("This is the site checker connectivity")

#get the url and store in a variable
site_url = input("Enter your site url to check:\n")

# import urllib.request to get the data from the url
# write a function that takes a url
def main(url):
    print("Checking connection...")
    #open the url open
    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully!")
    print(f"The response code was {response.getcode()}")




# returns a response