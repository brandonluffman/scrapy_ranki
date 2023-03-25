import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["https://www.google.com/shopping/product/2934641822888570258?q=jabra+elite+75t&prds=eto:7775744292317797311_0;227012557280341361_0;15650209205817740210_0,pid:17956440278338105789,rsk:PC_17376202431123258754&sa=X&ved=0ahUKEwiq9pfGm_f9AhUMMVkFHStAAp4Q9pwGCA8"]

    def parse(self, response):
        descriptions = response.css('div.sg-product__dpdp-c')
        product_title = descriptions.css('span.BvQan::text').get()
        product_description = descriptions.css('span.sh-ds__full-txt::text').get()
        product_rating = descriptions.css('div.uYNZm::text').get()
        product_review_count = descriptions.css('div.qIEPib::text').get().replace(' reviews','')
        product_img = descriptions.css('div.Xkiaqc img').attrib['src']
        product_specs = descriptions.css('td.crbkUb::text').getall()
        product_descs = descriptions.css('td.hCi1Vc::text').getall()
        product_all_reviews_link = 'https://google.com' + descriptions.css('a.Ba4zEd').attrib['href']
        product_purchase_stores = descriptions.css('a.b5ycib::text').getall()
        # product_buying_options = 'https://google.com' + descriptions.css('a.LfaE9').attrib['href']


        try:
            product_buying_options = 'https://google.com' + descriptions.css('a.LfaE9').attrib['href']
        except:
            product_buying_options = []
            diver = descriptions.css('div.UAVKwf')
            for div in diver:
                test = div.css('a').attrib['href']
                product_buying_options.append(test)
            print(product_buying_options)

        # self.review_links.append(product_all_reviews_link)
        # self.buying_option_links.append(product_buying_options)

        if ',' in product_review_count:
            product_review_count = product_review_count.replace(',', '')
        else:
            pass
        yielder = {
                    'product_title' : product_title,
                    'product_description' : product_description,
                    'product_rating' : float(product_rating),
                    'review_count' : int(product_review_count),
                    'product_img' : product_img,
                    'product_specs' : product_specs,
                    'product_descs' : product_descs, 
                    'all_reviews_link': product_all_reviews_link,
                    'product_purchase_stores' : product_purchase_stores,
                    'product_buying_options' : product_buying_options,
            }
        print(yielder) 
