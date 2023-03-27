import scrapy
import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

r = requests.get('https://www.rtings.com/headphones/reviews/best/headphones', headers=headers)

soup = BeautifulSoup(r.text, 'lxml')
print("Affiliate Content")
affiliate_content = []
for heading in soup.find_all(["h1", "h2","h3","h4","h5","h6","li" ,"p"]):
    # print(heading.name + ' ' + heading.text.strip())
    # print(f' -------- \n')
    if len(heading.text.strip()) > 20:
        affiliate_content.append(" ".join(heading.text.strip().replace('\n', '').split()))
        print(" ".join(heading.text.strip().replace('\n', '').split()))
    else:
        pass

print(affiliate_content)