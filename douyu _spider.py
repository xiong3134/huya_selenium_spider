from selenium import webdriver
import json
import time
class HuyaSpider:
    def __init__(self):
       self.url="https://www.huya.com/l"
       self.driver = webdriver.Chrome()


    def get_content_list(self):
        li_list=self.driver.find_elements_by_xpath(".//div[@class='box-bd']/ul/li")
        content_list=[]
        for li in li_list:
            item={}
            item['img']=li.find_element_by_xpath("./a[1]/img").get_attribute('src')
            item['title']=li.find_element_by_xpath("./a[contains(@class,'title')]").get_attribute('title')
            item['nick']=li.find_element_by_xpath(".//i[@class='nick']").get_attribute('title')
            item['js_num'] = li.find_element_by_xpath(".//i[@class='js-num']").text
            item['category']=li.find_element_by_xpath(".//span[contains(@class,'game-type')]/a").text
            content_list.append(item)
            print(item)
        next_url =self.driver.find_element_by_xpath(".//a[@class='laypage_next']")




        return content_list,next_url
    def save_content_list(self,content_list):
        with open('test.json', 'w', encoding='utf-8') as fp:
            json.dump(content_list, fp,ensure_ascii=False)



    def run(self):
        self.driver.get(self.url)
        content_list,next_url=self.get_content_list()
        self.save_content_list(content_list)
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list,next_url=self.get_content_list()
            self.save_content_list(content_list)

if __name__ =="__main__":
    huya = HuyaSpider()
    huya.run()

