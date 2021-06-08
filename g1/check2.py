from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import send_mail


def do_check(driver, link, word):
    driver.get(link)
    time.sleep(1)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    items = re.findall(r'class="grid-card__title">(.*?)<', str(soup))
    links = re.findall(r'<a class="grid-card__inner" href="(.*?)"', str(soup))
    prices = re.findall(r'span class="price-display">(.*?)</span', str(soup))
    found = False
    count = 0
    found_links = ''
    for name in items:
        if word in name.lower():
            found = True
            found_links += word + ' found: ' + links[count]+ " " + prices[count] + '\n\n'
        count += 1
    return found, found_links


def check_words():
    driver1 = webdriver.Chrome(executable_path=r'../g1/chromedriver')
    # put in desired url. right now set to pedals
    url = 'https://reverb.com/marketplace?product_type=effects-and-pedals&condition=used'
    # used boss for testing purposes. words_to_check is where you input desired words
    words_to_check = [ 'boss' , 'ds-1']
    results = ''
    for word in words_to_check:
        found, link = do_check(driver1, url, word)
        if found:
            results = results + str(link) + '\n '
    print(results)
    if results != '':
        send_mail.send_email('Found search terms ', str(results))
    #driver1.close()


if __name__ == '__main__':
    check_words()