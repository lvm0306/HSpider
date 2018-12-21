from utils.SpiderUtil import *
base='https://www.566ii.com/shipin/list-%E4%BA%9A%E6%B4%B2%E6%97%A0%E7%A0%81.html'
def getVideoUrl():
    html=SpiderHtml(base).getHtml()
    print(html)






if  __name__=="__main__":
    getVideoUrl()
    print()