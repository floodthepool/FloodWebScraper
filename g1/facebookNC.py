from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import send_mail


def do_check(driver, link):
    driver.get(link)
    time.sleep(1)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    #print(str(soup))
    # only checking if one of the top 4 is new, otherwise slow checking a lot of old stuff.
    # basically, we know that if we havent checked in a while (i.e. before a run of the system) then there will be a lot of new ones
    # but if we are running automatically, realistically only 1 will pop up (at the very extreme 4) within our 30 second period
    # so only checking the most recent 4 would be worth it, saving lots of computing time
    string = re.findall(r'class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7" style="-webkit-box-orient:vertical;-webkit-line-clamp:2;display:-webkit-box">(.*?)</span></span></div></span></div><div', str(soup))[1:8]
    price = re.findall(r'class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb iv3no6db a5q79mjw g1cxx5fr lrazzd5p oo9gr5id" dir="auto">(.*?)</span></div></span></div><div', str(soup))[1:8]
    #ids = [x.split('"')[0] for x in string]
    #links = [x.split('"')[2] for x in string]
    #names = [x.split('>')[1] for x in string]

    found_links = ''
    f = open('already_fb_NC', 'r')
    x = f.read()
    count = 0
    found = False
    for idd in string:
        if idd not in x:
            found = True
            found_links += string[count] + ': ' + price[count] + '\n\n'
        count += 1
    f.close()
    f = open('already_fb_NC', 'w')
    f.write(str(string))
    f.close()
    new = False
    return found, found_links

def check_fb():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver1 = webdriver.Chrome(executable_path=r'../g1/chromedriver', options=options)
    # put in desired url. right now set to pedals
    url = 'https://www.facebook.com/marketplace/105696062797469/instruments/?daysSinceListed=1&deliveryMethod=local_pick_up&sortBy=creation_time_descend&exact=false'
    url_base = 'https://washingtondc.craigslist.org/search/msg?query='
    extra = '-cymbal+-horns+-violin+-drum+-flute+-piano+-horn+-keybord+-ukelele+-saxophone+-trumpet+-alto+-sax&purveyor-input=owner'
    # used boss for testing purposes. words_to_check is where you input desired words
    results = 'New items: '
    found, link = do_check(driver1, url)
    if found:
        results = results + str(link) + '\n '
    else:
        return
    print(results)
    if results != '':
        send_mail.send_email('Found new items facebook NC', str(results))
    driver1.close

def try_fb():
    try:
        options = webdriver.ChromeOptions()
        options.headless = True
        driver1 = webdriver.Chrome(executable_path=r'../g1/chromedriver', options=options)
        # put in desired url. right now set to pedals
        url = 'https://www.facebook.com/marketplace/105696062797469/instruments/?daysSinceListed=1&deliveryMethod=local_pick_up&sortBy=creation_time_descend&exact=false'
        url_base = 'https://washingtondc.craigslist.org/search/msg?query='
        extra = '-cymbal+-horns+-violin+-drum+-flute+-piano+-horn+-keybord+-ukelele+-saxophone+-trumpet+-alto+-sax&purveyor-input=owner'
        # used boss for testing purposes. words_to_check is where you input desired words
        results = 'New items: '
        found, link = do_check(driver1, url)
        if found:
            results = results + str(link) + '\n '
        else:
            return
        print(results)
        if results != '':
            send_mail.send_email('Found new items facebook NC', str(results))
        driver1.close
    except:
        print('wifi failed')



if __name__ == '__main__':
    check_fb()
