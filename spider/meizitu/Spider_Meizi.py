from utils.SpiderUtil import SpiderHtml


def runSpider(url):
    html = SpiderHtml(url).getHtml()
    print(html)


if __name__ == "__main__":
    runSpider('https://www.mzitu.com/all')
