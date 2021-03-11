import scrapy


class WallpaperspiderSpider(scrapy.Spider):
    name = 'WallpaperSpider'
    allowed_domains = ['wall.alphacoders.com']
    start_urls = ['http://wall.alphacoders.com/search.php?search=breaking+bad/']
    page_num= 1
    def parse(self, response):
        # Get Img tags
        img_tags= response.css('img.img-responsive')
        thumb_urls= []
        # Fetech Thumbnail urls
        for i in img_tags:
            thumb_urls.append(i.attrib['src'])
        # Convert Thumbnail urls to Wallpaper img ursl
        img_urls= [t.replace("thumbbig-","") for t in thumb_urls]
        
        for i in img_urls:
            yield { 'urls':i }
        self.page_num= self.page_num+1
        next_page_url= "https://wall.alphacoders.com/search.php?search=breaking+bad&page="+ str(self.page_num)

        yield response.follow(next_page_url ,callback=self.parse)