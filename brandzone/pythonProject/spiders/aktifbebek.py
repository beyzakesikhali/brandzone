import scrapy
from ..items import PythonprojectItem
class aktifBebek(scrapy.Spider) :
    name = 'aktifbebek'
    pageNumber = 1
    barcodeUrls=[]
    start_urls = [
        'https://www.aktifbebek.com/bebek-bakimi-ve-banyo'
    ]

    def parse(self, response):
        items=PythonprojectItem()
        x=1
        aktifBebek.barcodeUrls=response.xpath("//a[@class='name']/@href").getall()
        #aktifBebek.barcodeUrls=response.xpath("//a[@class='name']/@href").getall()
        if len(aktifBebek.barcodeUrls)>0:
            yield response.follow(url=aktifBebek.barcodeUrls[x], callback=self.parse)
            x+=1
            aktifBebek.barcodeUrls.pop(x)

        for productUrl in aktifBebek.barcodeUrls:
            print("barcodeUrl", productUrl)
            product = response.xpath("//div[@class='product']")
            print("product extract",product)
            brand=product.xpath("//a[@class='brand']/text()").get()
            print("brand",brand)
            productName=product.xpath("//h2[@class='theme-h2']/text()").extract()
            print("productName",productName)
            image=product.xpath("//img/@src").get()
            print("image",image)
            items["name"]=productName
            items["brand"]=brand
            items["image"]=image
            items["url"]=productUrl
            print("ITEMS",items)
            yield items

        if aktifBebek.pageNumber<3 :
            print("pageNumber:",aktifBebek.pageNumber)
            aktifBebek.pageNumber += 1
            next_page='https://www.aktifbebek.com/bebek-bakimi-ve-banyo?Kategori=13&sayfa='+str(aktifBebek.pageNumber)
            print("next_Page",next_page)
            yield response.follow(url=next_page, callback=self.parse)







