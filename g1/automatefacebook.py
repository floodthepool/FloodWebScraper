import facebook
import facebookNC
import schedule

facebook.try_fb()
facebookNC.try_fb()

schedule.every(30).seconds.do(facebook.try_fb)
schedule.every(30).seconds.do(facebookNC.try_fb)


while True:
    schedule.run_pending()
