import scrapy
from ..items import PythonprojectItem
class aktifBebek2(scrapy.Spider) :
    name = 'aktifbebek2'
    pageNumber = 1
    start_urls = [
        'https://www.aktifbebek.com/bebek-bakimi-ve-banyo'
    ]

    def parse(self, response):
        items=PythonprojectItem()
        productsList=response.xpath("//div[@class='products-list']")
        productsItem=productsList.xpath("//div[@class='products-item']")

        print("productItem: ", aktifBebek2.pageNumber,"  ","len: ",len(productsItem),productsItem.extract())

        for product in productsItem:
            print("product beyza","page:", aktifBebek2.pageNumber, product.extract())
            productName= product.css('a[class*=name] ::text').get()
            print("productName mehmet",productName)
            brand=product.css('a[class*=brand] ::text').get()
            print("brand me ",brand)
            barcode=product.css("p::text").get()
            print("barcode meh",barcode)
            image=product.css('img::attr(data-src)').get()
            print("image mehm",image)
            productUrl= response.css("a[class*=name] ::attr(href)").get()

            items["name"]=productName
            items["brand"]=brand
            items["image"]=image
            items["barcode"]=barcode
            items["url"]=productUrl

        if aktifBebek2.pageNumber<3 :
            print("pageNumber:",aktifBebek2.pageNumber)
            aktifBebek2.pageNumber += 1
            next_page='https://www.aktifbebek.com/bebek-bakimi-ve-banyo?Kategori=13&sayfa='+str(aktifBebek2.pageNumber)
            print("next_Page",next_page)
            yield response.follow(url=next_page, callback=self.parse)









