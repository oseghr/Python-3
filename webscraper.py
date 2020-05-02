#Learning web scraping

import requests
from bs4 import BeautifulSoup

# result = requests.get("https://www.whitehouse.gov/briefings-statements/")

result = requests.get("https://www.whitehouse.gov/about-the-white-house/presidents/")
src = result.content
soup = BeautifulSoup(src, "html.parser")
#to make the prints beautiful
soup.prettify()

urls = []

#targets the ordered lists of presidents
list = soup.find("ol")
#targets each item in the lists 
link = list.find_all('li')

word = ''

for name in link:
    link = name.find('a')
    word = link.get_text()
    urls.append(word)

    
#Gets the links to presidents
# for name in link:
#     link = name.find('a')
#     urls.append(link.attrs['href'])


#prints the names of presidents
print(urls)





#Test web scraping lesson 2
# import requests
# from bs4 import BeautifulSoup

# result = requests.get("https://www.google.com/")
# print("Status Code:", result.status_code)
# src = result.content
# print(result.headers)
# soup = BeautifulSoup(src, "html.parser")

# links = soup.find_all("a")
# print(links)
# print("\n")

# for link in links:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs['href'])





