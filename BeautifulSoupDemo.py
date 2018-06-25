from urllib.request import urlopen
from bs4 import BeautifulSoup

# Open url, and get the content from the html
html = urlopen('https://github.com/Xiaoxiao-Liu')  
# Feed the content we get to the BeautifulSoup object
bs_obj=BeautifulSoup(html.read(), 'html.parser')
# Find all tags of class="nav-item-primary"
text_list=bs_obj.find_all("ul","vcard-details border-top border-gray-light py-3")

# Let's print them out
for text in text_list:
    print(text.get_text())

html.close()
