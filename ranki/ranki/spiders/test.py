# import scrapy
# from tld import get_tld
# 0
# class TestSpider(scrapy.Spider):
#     name = "test"
#     start_urls = ["https://www.google.com/shopping/product/1219922484318508456?biw=2160&bih=1053&output=search&q=apple+airpods+max&oq=apple+airpods+max&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIIxAnMgQIIxAnMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQAFgAYN0CaABwAHgAgAFDiAFDkgEBMZgBAMABAQ&sclient=products-cc&prds=eto:6274634352930567101_0,pid:12252833144158501899,rsk:PC_7069147378898153804&sa=X&ved=0ahUKEwjE0d2-iY7-AhVfEVkFHU3CDqsQ9pwGCCk"]

#     def parse(self, response):
#         tds = response.css('div.UAVKwf')
#         linkers = []
#         for td in tds:
#             link = td.css('a').attrib['href']
#             linkers.append(link[7:])

#         # print(linkers)
 
#         resers = []
#         for url in linkers:
#             res = get_tld(url,as_object=True)
#             reser = res.fld
#             resers.append(reser)
#         print(resers)
#         i=0
#         newy = []
#         iland = []
#         for re in resers:
#             print(f'{re} i = {i}')
#             if re not in newy:
#                 newy.append(re)
#                 iland.append(linkers[i])
#             i +=1

#         print(iland)


