
import craig

import schedule


craig.check_craig()


schedule.every(2).minutes.do(craig.try_craig)


while True:
    schedule.run_pending()
