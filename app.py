import csv

from selenium import webdriver
from time import sleep

import config

driver_path = './chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

class Scraping(object):
    
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def decorator_open_top(func):
        """
        一休レストランのトップページのURLを取得し、開く
        """
        def open_top(*args, **kwargs):
            top_url = config.top_url
            driver.implicitly_wait(1)
            driver.get(top_url)
            restaurant_top_url = func(*args, **kwargs)
            return restaurant_top_url
        return open_top

    @decorator_open_top
    def search_restaurant(self):
        """
        トップページからレストラン名を入力し検索。検索結果の店のトップページに移動。
        """
        top_search_button_xpath = config.top_search_button_xpath
        driver.implicitly_wait(1)
        top_search_button = driver.find_element_by_xpath(top_search_button_xpath)
        driver.implicitly_wait(1)
        top_search_button.click()
        driver.implicitly_wait(3)
        search_space = driver.find_element_by_xpath(config.search_space_xpath)
        driver.implicitly_wait(1)
        search_space.click()
        driver.implicitly_wait(1)
        search_space.send_keys(self.restaurant)
        driver.implicitly_wait(1)
        search_restaurant_button = driver.find_element_by_xpath(config.search_restaurant_button_xpath)
        driver.implicitly_wait(1)
        search_restaurant_button.click()
        driver.implicitly_wait(1)
        search_result = driver.find_element_by_xpath(config.search_result_xpath)
        driver.implicitly_wait(1)
        search_result.click()
        driver.implicitly_wait(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(3)

    @staticmethod
    def get_comments():
        """
        店のクチコミボタンを押して、コメントをリスト化
        """
        comments_button = driver.find_element_by_xpath(config.comments_button_xpath)
        driver.implicitly_wait(1)
        comments_button.click()
        driver.implicitly_wait(1)
        elements = driver.find_elements_by_class_name(config.comments_class_name)
        comments = []
        for element in elements:
            comments.append(element.text)
        # 確認用のコード
        # for comment in comments:
        #     print(comment)
        # print(comments)
        return comments

class Csv(object):
    
    def __init__(self, comment_list):
        self.comment_list = comment_list
        
    def make_csv(self):
        with open('commens.csv', 'w') as csv_file:
            fieldnames = ['comment']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for comment in self.comment_list:
                writer.writerow({'comment': comment})
    


if __name__ == '__main__':
    scraping = Scraping('うしのほね　あなざ')
    restaurant_top_url = scraping.search_restaurant()
    comment_list = Scraping.get_comments()
    about_csv = Csv(comment_list)
    about_csv.make_csv()
    