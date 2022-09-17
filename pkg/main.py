from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    url = "http://quotes.toscrape.com/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html,"html.parser")

    quotes = soup.find_all(class_ = "text")
    
    print("Quotes present in the webistes are given below:\n")
    for x in quotes:
        print(x.string)

    print("\nThe authors of above quotes:\n")
    authors = set(soup.find_all(class_ = "author"))

    for i in authors:
        print(i.string)

if __name__ == "__main__":
    main()