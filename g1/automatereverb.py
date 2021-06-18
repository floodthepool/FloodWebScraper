import check3

import schedule

check3.try_check()
check3.wipe_file()

schedule.every(2).minutes.do(check3.try_check)
schedule.every(2).hours.do(check3.wipe_file)


while True:
    schedule.run_pending()
