import scrapy
# from tld import get_tld

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["https://www.google.com/shopping/product/17653315832884157286/offers?q=sony+wh1000xm5&prds=eto:8676632268192045111_0;4695355544304054685_0;3696208797495415788_0,pid:18209137397974619706,rsk:PC_11648784580466805463&sa=X&ved=0ahUKEwj4kYCVtJD-AhXQF1kFHUpoBGUQoLAGCNYB"]

    
    def parse(self, response):
        test = []
        tds = response.css('td.SH30Lb')
        for td in tds:
            Link = td.css('div.UAVKwf a::attr(href)').extract()
            test.append(Link)

        spans = response.css('td.SH30Lb')
        for td in spans:
            if td.css('span.fObmGc::text').extract() is not None:
                link = td.css('span.fObmGc::text')
                if link is not None:
                # test.append(t.extract())
                    test.append(link.extract())
                else:
                    continue
            else:
                continue

        list2 = [x for x in test if x]
 

        print(list2)













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


