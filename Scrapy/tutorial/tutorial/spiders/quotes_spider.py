import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.netflix.com/login'
        # 'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'stevedstigler@gmail.com', 'password': 'tigerpaw50'},
            callback=self.after_login
        )

    def after_login(self, response):
        print("You made it this far...")
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }