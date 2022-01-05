import scrapy
from bs4 import BeautifulSoup
import pandas as pd

class amazon_code_scrape(scrapy.Spider):

    name = "amazon_code_scrape"

    def start_requests(self):

        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        urls = [
        'https://yofreesamples.com/amazon-deals/amazon-promo-coupon-codes-list-today',
        ]

        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        item_list = response.css(".col-xs-9").getall()
        data_list = []

        for item in item_list:
            parsed_data = BeautifulSoup(item, features="lxml")
            title = parsed_data.body.find('h4', attrs={'class':'deal_title'}).text
            amz_link = parsed_data.body.find('a', href=True)['href']
            price = "$"+str(parsed_data.body.find('span', attrs={'class':'price'}))[20:-7]
            code = parsed_data.body.find('strong').text
            pctoff = parsed_data.body.find('span', attrs={'class':'pctoff'}).text + "%"
            item_dict = {'Product Title':title, 'Price':price, '% Off' :pctoff, 'Discount Code':code, 'Amazon_link':amz_link}
            data_list.append(item_dict)

        items_dataframe = pd.DataFrame(data_list)
        items_dataframe.to_csv(r"C:\Users\thisi\Desktop\amazon_code_scrape\output.csv", encoding='utf-8', index=False)
        print(items_dataframe)
