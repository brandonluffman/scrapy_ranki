# List = open('cats.txt').read().splitlines()
# print(List)

from tld import get_tld
 
linkers = ['https://www.honchosearch.com/blog/seo/how-to-get-root-domains-from-urls-using-python/', 'https://www.honchosearch.com/blog/seo/how-to-get-root-domains-from-urls-using-python/', 'https://www.honchosearch.com/blog/seo/how-to-get-root-domains-from-urls-using-python/', 'https://google.com']
resers = []
for url in linkers:
    res = get_tld(url,as_object=True)
    reser = res.fld
    resers.append(reser)
print(resers)
i=0
newy = []
iland = []
for re in resers:
    print(f'{re} i = {i}')
    if re not in newy:
        newy.append(re)
        iland.append(linkers[i])
    i +=1

print(newy)
print(iland)
