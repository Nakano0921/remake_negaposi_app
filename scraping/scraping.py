import chromedriver_binary
from selenium import webdriver
from time import sleep

import const

class Scraping(object):
    def __init__(self, res_name):
        self.res_name = res_name

    def set_driver(self):
        driver = webdriver.Chrome()
        return driver

    def open_restaurant(self, driver):
        """
        一休レストランのTOPを開く
        店名を指定して、クチコミを表示
        """
        # 一休レストランのTOPを開く
        driver.implicitly_wait(10)
        driver.get(const.top_url)
        driver.implicitly_wait(10)
        # 店名の検索
        top_search = driver.find_element_by_xpath(const.top_search)
        driver.implicitly_wait(10)
        top_search.click()
        driver.implicitly_wait(10)
        specific_xpath = driver.find_element_by_xpath(const.specific_xpath)
        driver.implicitly_wait(10)
        specific_xpath.click()
        driver.implicitly_wait(10)
        specific_xpath.send_keys(self.res_name)
        driver.implicitly_wait(10)
        search_button = driver.find_element_by_xpath(const.search_button)
        driver.implicitly_wait(10)
        search_button.click()
        driver.implicitly_wait(10)
        # クチコミ表示
        try:
            search_result = driver.find_element_by_class_name('noResult_XKws4').text
            print('検索されたお店は現在取得できません。')
        except:
            search_result = driver.find_element_by_xpath(const.search_result)
            search_result.click()
            sleep(3)
            tab_array = driver.window_handles
            driver.switch_to.window(tab_array[1])
            driver.implicitly_wait(10)
            review_xpath = driver.find_element_by_xpath(const.review_xpath)
            driver.implicitly_wait(10)
            review_xpath.click()
            sleep(1)
            more_info = driver.find_element_by_xpath(const.more_info)
            driver.implicitly_wait(10)
            more_info.click()
            driver.implicitly_wait(10)
            cur_url = driver.current_url
            return cur_url

    def get_item(self, driver, cur_url):
        """
        コメント、味、雰囲気、サービス、コスパを取得、リスト化
        """
        driver.get(cur_url)
        driver.implicitly_wait(10)
        toppage_xpath = driver.find_element_by_xpath(const.toppage_xpath)
        driver.implicitly_wait(10)
        toppage_xpath.click()
        driver.implicitly_wait(10)
        assesments = driver.find_elements_by_class_name("des_gdIDUsrImprBox")
        driver.implicitly_wait(10)
        i = 4
        c = 0
        n = 3
        while c < 3:
            for assesment in assesments:
                if i == 24:
                    break
                try:
                    comment = assesment.find_element_by_xpath(
                        f'//*[@id="des_inner"]/div[{i}]/div[3]/table/tbody/tr[3]/td'
                    ).text
                    comments.append(comment)
                except:
                    comment = assesment.find_element_by_xpath(
                        f'//*[@id="des_inner"]/div[{i}]/div[3]/table/tbody/tr[2]/td'
                    ).text
                    comments.append(comment)
                taste = assesment.find_element_by_xpath(
                    f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[2]/td[2]/span'
                ).text
                tastes.append(taste)
                service = assesment.find_element_by_xpath(
                    f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[3]/td[2]/span'
                ).text
                services.append(service)
                mood = assesment.find_element_by_xpath(
                    f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[4]/td[2]/span'
                ).text
                moods.append(mood)
                cospa = assesment.find_element_by_xpath(
                    f'//*[@id="des_inner"]/div[{i}]/div[1]/table/tbody/tr[5]/td[2]/span'
                ).text
                cospas.append(cospa)
                i += 2
            if c == 0:
                next_page = driver.find_element_by_xpath(
                    '//*[@id="des_inner"]/div[24]/a[1]'
                )
                driver.implicitly_wait(10)
                next_page.click()
                driver.implicitly_wait(10)
                assesments = driver.find_elements_by_class_name("des_gdIDUsrImprBox")
                c += 1
                i = 4
            elif c == 1 or c == 2:
                next_page = driver.find_element_by_xpath(
                    f'//*[@id="des_inner"]/div[24]/a[3]'
                )
                driver.implicitly_wait(10)
                next_page.click()
                driver.implicitly_wait(10)
                assesments = driver.find_elements_by_class_name("des_gdIDUsrImprBox")
                c += 1
                i = 4

if __name__ == "__main__":
    scraping = Scraping('NARISAWA')
    driver = scraping.set_driver()
    cur_url = scraping.open_restaurant(driver)
    comments = []
    tastes = []
    services = []
    moods = []
    cospas = []
    scraping.get_item(driver, cur_url)