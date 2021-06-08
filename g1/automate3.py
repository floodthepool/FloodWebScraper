
import craig2
import schedule


craig2.check_craig()

schedule.every(15).seconds.do(craig2.check_craig)

while True:
    schedule.run_pending()
