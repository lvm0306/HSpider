import matplotlib.pyplot as plt

from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba
import numpy as np
from PIL import Image


class CiyunHelper():
    """
    本地文本生成词云
    texturl ： 本地文档地址
    imageur ： 生成图片的地址
    """

    def __init__(self, texturl, imageurl, width, height, fontsize):
        self.texturl = texturl
        self.imageurl = imageurl
        self.width = width
        self.height = height
        self.fontsize = fontsize

    def createImage(self):
        text = open(self.texturl).read()
        jieba_text = jieba.cut(text, cut_all=True)
        text_after = " ".join(jieba_text)
        wordcloud = WordCloud(background_color="white",
                              width=self.width,
                              height=self.height,
                              font_path='D:\\space\\py_space\\spider\\spider\\qishus\\y245.ttf',  # 字体设置 不写中文乱码
                              margin=4,  # 边距
                              max_font_size=self.fontsize,  # 设置字体最大值
                              random_state=160,  # 设置有多少种随机生成状态，即有多少种配色方案
                              scale=.5,
                              max_words=300
                              ).generate(text_after)
        wordcloud.to_file(self.imageurl)

    def show(self):
        text = open(self.texturl).read()
        wordcloud = WordCloud(background_color="white",
                              width=self.width,
                              height=self.height,
                              font_path='D:\\space\\py_space\\spider\\spider\\qishus\\y245.ttf',  # 字体设置 不写中文乱码
                              margin=2,  # 边距
                              max_font_size=self.fontsize,  # 设置字体最大值
                              random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                              scale=.5
                              ).generate(text)

        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()


class CiyunHelperBg():
    def __init__(self, texturl, imageurl, width, height, fontsize, backgroundimage):
        self.texturl = texturl
        self.imageurl = imageurl
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.backgroundimage = backgroundimage

    def createImage(self):
        mask = np.array(Image.open(self.backgroundimage))
        text = open(self.texturl).read()
        wordcloud = WordCloud(background_color="white",
                              width=self.width,
                              height=self.height,
                              mask=mask,
                              font_path='D:\\space\\py_space\\spider\\spider\\qishus\\y245.ttf',  # 字体设置 不写中文乱码
                              margin=2,  # 边距
                              max_font_size=self.fontsize,  # 设置字体最大值
                              random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                              scale=.5
                              ).generate(text)
        wordcloud.to_file(self.imageurl)

    def show(self):

        mask = np.array(Image.open(self.backgroundimage))
        text = open(self.texturl).read()
        wordcloud = WordCloud(background_color="white",
                              width=self.width,
                              height=self.height,
                              mask=mask,
                              font_path='/Users/lovesosoi/Documents/font_style/syst.otf',  # 字体设置 不写中文乱码
                              margin=2,  # 边距
                              max_font_size=self.fontsize,  # 设置字体最大值
                              random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                              scale=.5
                              ).generate(text)


        image_colors = ImageColorGenerator(mask)
        plt.figure()
        plt.imshow(wordcloud.recolor(color_func=image_colors))
        plt.axis("off")
        plt.show()