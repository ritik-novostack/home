import scrapy
from ..items import HomeItem
import time

class home_deport(scrapy.Spider):
    name="homedepot"

    allowed_domains = ['homedepot.com']

    def __init__(self , url='',*args,**kwargs):
    
        
        self.start_urls=[url]

    
    def parse(self, response):
        items=HomeItem()
        internet_no=response.xpath('//*[@id="root"]/div/div[3]/div/div/div[2]/div/div[1]/div/div/h2[1]/text()')[1].extract()
        model_no=response.xpath('//*[@id="root"]/div/div[3]/div/div/div[2]/div/div[1]/div/div/h2[2]/text()')[1].extract()
        product_name=response.xpath('//*[@id="root"]/div/div[3]/div/div/div[3]/div[1]/div/div[1]/div/div/div[1]/span/h1/text()').extract_first()
        product_price=str(response.xpath('//*[@id="standard-price"]/div/div/span[2]/text()').extract_first())+"."+str(response.xpath('//*[@id="standard-price"]/div/div/span[3]/text()').extract_first())
        javascript = response.css("script")[9].extract()
        image_urls=javascript[javascript.find('["')+1:javascript.find('"]')+1].replace('"','').split(",")
        image_urls=[i[:i.rfind("_")+1]+"6"+i[i.rfind("_")+2:]   for i in image_urls]
        
        items['product_title'] =product_name 
        items['product_url'] = response.url
        items['product_sub_title'] =""
        items['product_price'] = '$'+product_price
        items['model_number'] = model_no
        items['internet_no']=internet_no
        # the images are repeating so filtering the unique
        items['images'] = image_urls

        items['fetched_at'] = time.strftime('%d-%m-%Y %H:%M:%S')

        yield items

        
        
