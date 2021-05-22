"""
app.pyで使うURLやxpathなどの長い文字列が値の変数をまとめているファイル
"""
# 一休レストランのトップページのURL
top_url = 'https://restaurant.ikyu.com/?medium_area_code=03001&visit_date=2021-05-23&visit_time=19%3A00&expand_visit_minutes=60&num_guests=2'
# トップページの「検索」ボタンのxpath
top_search_button_xpath = '//*[@id="__layout"]/div/main/div[2]/section[1]/div[2]/button'
# トップページの「検索」ボタンを押した後に移動したページの「「エリア、ジャンル、店名」のスペースのxpath
search_space_xpath = '//*[@id="__layout"]/div/div[2]/div/aside/div[2]/form/div/div/div/input'
# 「🔍」ボタンのxpath
search_restaurant_button_xpath = '//*[@id="__layout"]/div/div[2]/div/aside/div[2]/form/div/div/button'
# 検索結果の1番上位の店のxpaht
search_result_xpath = '//*[@id="__layout"]/div/div[2]/div/main/section/a'