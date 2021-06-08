
import craig

import schedule


craig.check_craig()


schedule.every(15).seconds.do(craig.check_craig)


while True:
    schedule.run_pending()
