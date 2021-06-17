from bs4 import BeautifulSoup
from selenium import webdriver
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
    #print(items)
    found = False
    count = 0
    found_links = ''
    f = open('already_found', 'r')
    x = f.read().split(',')
    for name in items:
        if word in name.lower() and links[count] not in x:
            print(links[count])
            found = True
            found_links += word + ' found: ' + links[count] + " " + prices[count] + '\n\n'
            x.append(links[count])
        count += 1
    f.close()
    x =','.join(x)
    f =open('already_found', 'w')
    f.write(x)
    f.close()
    return found, found_links


def check_words():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver1 = webdriver.Chrome(executable_path=r'../g1/chromedriver', options=options)
    # put in desired url. right now set to pedals
    url = 'https://reverb.com/marketplace?query=%20&condition=used'
    # used boss for testing purposes. words_to_check is where you input desired words
    words_to_check = ['contemporary stratocaster', 'mira x', 'starla x', 'shell pink', 'king of tone', 'allen amplification', 'oldfield', 'analogman', 'bass vi', 'keeley mod', 'JHS mod', 'grandma hannon', 'dimarzio' , 'seymour duncan', '| demo', 'baritone', 'kiesel', 'strandberg', 'vela semi hollow', 'vela semi-hollow', 'lollar', 'knaggs', 'mastery', 'staytrem', 'baby z', 'yamaha thr']
    results = ''
    for word in words_to_check:
        found, link = do_check(driver1, url, word)
        if found:
            results = results + str(link) + '\n '
    print(results)
    if results != '':
        send_mail.send_email(results, str(results))
    driver1.close()

def wipe_file():
    f = open('already_found', 'w')
    f.close

def try_check():
    try:
        options = webdriver.ChromeOptions()
        options.headless = True
        driver1 = webdriver.Chrome(executable_path=r'../g1/chromedriver', options=options)
        # put in desired url. right now set to pedals
        url = 'https://reverb.com/marketplace?query=%20&condition=used'
        # used boss for testing purposes. words_to_check is where you input desired words
        words_to_check = ['contemporary stratocaster', 'mira x', 'starla x', 'shell pink', 'king of tone',
                          'allen amplification', 'oldfield', 'analogman', 'bass vi', 'keeley mod', 'JHS mod',
                          'grandma hannon', 'dimarzio', 'seymour duncan', '| demo', 'baritone', 'kiesel', 'strandberg',
                          'vela semi hollow', 'vela semi-hollow', 'lollar', 'knaggs', 'mastery', 'staytrem', 'baby z',
                          'yamaha thr']
        results = ''
        for word in words_to_check:
            found, link = do_check(driver1, url, word)
            if found:
                results = results + str(link) + '\n '
        print(results)
        if results != '':
            send_mail.send_email(results, str(results))
        driver1.close()
    except:
        print('wifi failed, trying again in 15')


if __name__ == '__main__':
    check_words()