import scrape_copy
import schedule

scrape_copy.startfunc()

schedule.every(60).seconds.do(scrape_copy.startfunc)


while True:
    schedule.run_pending()
