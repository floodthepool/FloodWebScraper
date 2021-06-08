import check3

import schedule

check3.check_words()

schedule.every(15).seconds.do(check3.check_words)


while True:
    schedule.run_pending()
