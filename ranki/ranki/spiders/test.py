import scrapy
import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

cats = ['Over Ear Headphones', 'Earbuds', 'Smartphones', 'Tablets', 'Routers', 'Cameras', 'TV', 'Laptop', 'Bluetooth Speakers', 'Smart Watches', 'Home Security System', 'Mens Jeans', 'Womens Leggings', 'Mens Cardigans', 'Bras', 'Womens Underwear', 'Mens Underwear', 'Mens Gym Shorts', 'Mens gym shirts', 'Womens socks', 'Womens Swimsuits', 'Mens Swimsuits', 'Womens Blouses', 'Womens Workout tops', 'Mens running shoes', 'womens running shoes', 'mens hiking boots', 'womens hiking boots', 'mens dress shoes', 'womens heels', 'mens sneakers', 'womens sneakers', 'mens golf shoes', 'womens golf shoes', 'mens boots', 'womens boots', 'mens flip flops', 'womens flip flops', 'womens platform shoes', 'Accessories', 'Womens Bags', 'Womens Purses', 'Mens belts', 'womens belts', 'womens eyeglasses', 'mens eyeglasses', 'Mens sunglasses', 'womens sunglasses', 'beanies', 'wallets', 'mens hats', 'womens hats', 'womens necklaces', 'mens chains', 'mens bracelets', 'womens bracelets', 'womens earrings', 'mens earrings', 'mens rings', 'womens rings', 'Air Fryer', 'Humidifier', 'Comforter', 'Blender', 'Toaster', 'Water Bottle', 'Crock Pot', 'Food Scale', 'Skillet', 'Grill', 'Smoker', 'Pellet Grills', 'Food Storage Containers', 'Beauty & Personal Care', 'Sunscreen', 'Body Lotion', 'Face Lotion', 'Deodorant', 'Perfume', 'Cologne', 'Mens Razors', 'Womens Razors', 'Makeup Remover', 'Mascara', 'Lipstick', 'Chapstick', 'Nail Polish', 'Blow Dryer', 'Mens Electric Razor', 'Exfoliator', "Men's Body Wash", "Women's Body Wash", 'Womens Shampoo', "Men's Shampoo", 'Womens Conditioner', 'Mens Conditioner']

for cat in cats:
    serps = response.css('div.v7W49e')
    serp_results = serps.css('div.yuRUbf')
    serp_link_list = []
    if serp_results:
        for serp_result in serp_results[:3]:
            serp_link = serp_result.css('a').attrib['href']
            serp_link_list.append(serp_link)
    urls = []

for url in urls:    
    r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')
affiliate_content = []
for heading in soup.find_all(["h1", "h2","h3","h4","h5","h6","li" ,"p"]):
    # print(heading.name + ' ' + heading.text.strip())
    # print(f' -------- \n')
    if len(heading.text.strip()) > 20:
        affiliate_content.append(" ".join(heading.text.strip().replace('\n', '').split()))
        # print(" ".join(heading.text.strip().replace('\n', '').split()))
    else:
        pass
 
    final_content = " ".join(affiliate_content)
    
print(final_content)