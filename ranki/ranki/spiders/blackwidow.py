import scrapy
from collections import Counter
import datetime
from newspaper import Article
from newspaper import Config
import praw
from praw.models import MoreComments
import re
from scrapy import Request
import spacy
from youtube_transcript_api import YouTubeTranscriptApi


class BlackwidowSpider(scrapy.Spider):
    name = "blackwidow"

    def __init__(self, name=None, **kwargs):
        super(BlackwidowSpider,self).__init__(name, **kwargs) 
        self.results = {"entities": ['']}
        self.entities = ['sony wh-1000xm5', 'bose quietcomfort', 'apple airpods max']
        self.card_results = []
        self.review_links = []
        self.buying_option_links = []

    def start_requests(self):
        query = input("What would you like to get the links for? \n")
        today = datetime.date.today()
        year = today.year

        match = re.search(f'{year}', query)

        if 'best' not in query.lower() and match is None:
            query = 'best ' + query + ' ' + '2023'
        elif match is None:
            query = query + ' ' + '2023'
        elif 'best' not in query.lower():
            query = 'best ' + query
        else:
            pass
        remove = re.sub('(\A|[^0-9])([0-9]{4,6})([^0-9]|$)', '', query)
        google_query = query
        reddit_query = (remove + ' reddit')
        youtube_query = (query + ' youtube') 
        start_urls = ["https://www.google.com/search?q=" + google_query, "https://www.google.com/search?q=" + reddit_query, "https://www.google.com/search?q=" + youtube_query]
        card_urls = ['https://www.google.com/search?tbm=shop&q=' + product for product in self.entities]
        for url in start_urls:
            yield Request(url=url,callback=self.parse)
        for card_url in card_urls:
            yield scrapy.Request(url=card_url,callback=self.parse_cards)


    def parse(self, response):
        # NER MODEL
        # def get_product_names(self,response,text):
        #     # product_dummies = ['sony wh-1000xm4', 'jabra elite 75t', 'apple airpods max', 'sony wh-1000xm5']
        #     text = text.split()[:5]
        #     string = ''
        #     for i in text:
        #         string = string + i + ' ' 
        #     return string
            # nlp = spacy.load('./output/model-best')
            # doc = nlp(text)
            # items = [x.text for x in doc.ents]
            # Counter(items).most_common(10)
            # docs.append(doc)
            # return 

        serps = response.css('div.v7W49e')
        serp_results = serps.css('div.yuRUbf')
        serp_link_list = []
        if serp_results:
            for serp_result in serp_results:
                serp_link = serp_result.css('a').attrib['href']
                serp_link_list.append(serp_link)
        else:
            serp_results = serps.css('div.DhN8Cf')
            for serp_result in serp_results:
                serp_link = serp_result.css('a').attrib['href']
                serp_link_list.append(serp_link)

        # print(serp_link_list[0]) 

        metric_output = []
            
    
        if 'https://www.reddit.com' in serp_link_list[0]:
            # print('REDDIT LINK')
            # print("SERP LINK LIST", "----->", serp_link_list)
            reddit_read_only = praw.Reddit(client_id="6ziqexypJDMGiHf8tYfERA",         # your client id
                           client_secret="gBa1uvr2syOEbjxKbD8yzPsPo_fAbA",      # your client secret
                           user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")        # your user agent

            urls = serp_link_list
            
            # Creating a submission object

            url_to_comments = {}
            for url in urls:
                submission = reddit_read_only.submission(url=url)
            
                post_comments = []

                for comment in submission.comments[:10]:
                    if type(comment) == MoreComments:
                        continue
                    elif comment.body == '[removed]' or comment.body == '[deleted]':
                        continue
                    else:
                        post_comments.append(comment.body)
                # for comment in post_comments:
                #     get_product_names(response=response, self=self, text=comment)
                url_to_comments[url] = post_comments
            metric_output.append(url_to_comments)
            self.results['reddit'] = url_to_comments
            yield{
                'reddit': metric_output
            }

        elif 'https://www.youtube.com' in serp_link_list[0]:
            # print('YOUTUBE LINK')
            video_to_transcript = {}
            links = serp_link_list
            ids = []
            for link in links:
                id = link.replace('https://www.youtube.com/watch?v=', '')
                ids.append(id)

            video_ids = ids
            video_transcripts = {}
            for video_id in video_ids:
                video_transcripts[video_id] = YouTubeTranscriptApi.get_transcript(video_id)

            for item in video_transcripts.items():
                text = ''
                for i in item[1]:
                    text = text + i['text'] + ' '
                    video_transcripts[item[0]] = text
                    # get_product_names(response=response, self=self, text=text)
            for k,v in video_transcripts.items():
                video_to_transcript[k] = v
            self.results['youtube'] = video_to_transcript
            yield{
                'youtube': video_to_transcript
            }

        else:
            print('GOOGLE LINK')
            affiliate_to_text = {}    
            for serp_link in serp_link_list:
                print(serp_link)
                user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                config = Config()
                config.browser_user_agent = user_agent

                try:
                    article = Article(serp_link, config=config)
                    article.download()
                    article.parse()
                    affiliate_to_text[serp_link] = article.text
                    # get_product_names(response=response,self=self,text=article.text)
                except:
                    pass
            self.results['google'] = affiliate_to_text
            yield{
                'google': affiliate_to_text
            }

    def parse_cards(self, response):
        domain = 'https://www.google.com/'
        first_row = response.css('div.i0X6df')[:6]
        cards_with_stores = []
        for card in first_row:
            if card.css('a.iXEZD span::text').get() is not None:
                cards_with_stores.append(card)
            else:
                continue
        stores_count_per_card = []
        for card in cards_with_stores:
            num_stores = int(card.css('a.iXEZD span::text').get().replace('+',''))
            stores_count_per_card.append(num_stores)
        print(stores_count_per_card)
        max_num_of_stores = max(stores_count_per_card)
        cards_with_max_num_stores = []
        for card in cards_with_stores:
            num_stores = int(card.css('a.iXEZD span::text').get().replace('+',''))
            if num_stores == max_num_of_stores:
                cards_with_max_num_stores.append(card)
            else:
                continue
        if len(cards_with_max_num_stores) == 1:
            card = cards_with_max_num_stores[0]
            self.card_results.append(domain + card.css('div.sh-dgr__content span.C7Lkve a').attrib['href'])
        else:
            card_reviews_counts = []
            for card in cards_with_max_num_stores:
                review_count = int(card.css('span.QIrs8::text').get().split(" ")[-3].replace(',',''))
                card_reviews_counts.append(review_count)
            max_num_card_reviews = max(card_reviews_counts)
            for card in cards_with_max_num_stores:
                review_count = int(card.css('span.QIrs8::text').get().split(" ")[-3].replace(',',''))
                if review_count == max_num_card_reviews:
                    self.card_results.append(domain + card.css('div.sh-dgr__content span.C7Lkve a').attrib['href'])

        links = self.card_results
        for link in links:
            yield scrapy.Request(f'{link}', callback=self.parse_descriptions)

        if len(self.card_results) == len(self.start_urls):
            yield {
                'card_links': self.card_results
            }


    def parse_descriptions(self, response):
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
        product_buying_options = 'https://google.com' + descriptions.css('a.LfaE9').attrib['href']


        self.review_links.append(product_all_reviews_link)
        self.buying_option_links.append(product_buying_options)

        if ',' in product_review_count:
            product_review_count = product_review_count.replace(',', '')
        else:
            pass
            #here we put the data returned into the format we want to output for our csv or json file
        yield{
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
        # print(yielder)


        for review_link in self.review_links:
            yield scrapy.Request(f'{review_link}', callback=self.parse_reviews)
        
        
        for buying_link in self.buying_option_links:
            yield scrapy.Request(f'{buying_link}', callback=self.parse_buying_options)

    def parse_buying_options(self, response):
        tds = response.css('div.UAVKwf')
        for td in tds:
            links = td.css('a').attrib['href']
            if links:
                print(links)


    def parse_reviews(self, response):
        reviews = response.css('div.z6XoBf')
        
        for review in reviews:
            title = review.css('.P3O8Ne::text').get()
            date = review.css('.ff3bE::text').get()
            rating = int(review.css('.UzThIf::attr(aria-label)').get()[0])
            content = review.css('.g1lvWe div::text').get()
            source = review.css('.sPPcBf').xpath('normalize-space()').get()
            #here we put the data returned into the format we want to output for our csv or json file
            yield{
                'title' : title,
                'rating' : rating,
                'date' : date,
                'content' : content,
                'source' : source,
            }

            # next_page = response.css('.sh-fp__pagination-button::attr(data-url)').get()

            # if next_page is not None:
            #     # re-assigns requests.get url to a new page url
            #     next_page_url = 'https://www.google.com' + next_page
            #     yield response.follow(next_page_url, callback=self.parse_reviews)



        