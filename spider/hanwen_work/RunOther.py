import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

default_url = "https://per.spdb.com.cn/bank_financing/financial_product/?tdsourcetag=s_pctim_aiomsg"
chromer_driver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chromer_driver, options=option)
    driver.get(default_url)
    WebDriverWait(driver, 4)
    time.sleep(2)  # 获取到网页数据
    # driver.find_element_by_link_text(u"不限").click()
    # driver.find_element_by_xpath(u"(//a[contains(text(),'不限')])[2]").click()#点击两个不限

    driver.find_element_by_link_text(u"港币").click()
    div_1 = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div/div[3]/div[3]/div[2]/div/div')
    print(div_1[0].text == "")
    # a_c = [u"固定期限",u"私行专属",u"专属产品"]
    # a_e = ["xjgl","jzl","hlc",]
    # b = [u"即将发售",u"可购买",u"不可购买",u"已过期"]
    #
    # for i in a_c:
    #     for j in b:
    #         driver.find_element_by_link_text(i).click()
    #         driver.find_element_by_link_text(j).click()
    #         WebDriverWait(driver, 4)
    #         time.sleep(0.5)
    #         run(driver)
    #
    # for i in a_e:
    #     for j in b:
    #         driver.find_element_by_id(i).click()
    #         driver.find_element_by_link_text(j).click()
    #         WebDriverWait(driver, 4)
    #         time.sleep(0.5)
    #         run(driver)
